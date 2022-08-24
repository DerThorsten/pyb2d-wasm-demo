import pyjs
import b2d
import asyncio
from b2d.testbed.backend.gui_base import GuiBase
import functools
from b2d.testbed import TestbedBase
import time


def make_js_func(py_func):
    jspy = pyjs.JsValue(py_func)
    f = jspy.py_call.bind(jspy)
    return f, jspy

class PseudoMouseEvent(object):
    def __init__(self, touch_event):
        self.x = touch_event.clientX
        self.y = touch_event.clientY


class ExplicitPseudoEvent(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y

class CanvasAsyncGui(GuiBase):
    class Settings(GuiBase.Settings):
        class Config:
            arbitrary_types_allowed = True


    def __init__(self, testbed_cls, settings, testbed_settings=None):
        print("v4")

        self.settings = settings
        self.resolution = self.settings.resolution

        # steping settings
        self._fps = settings.fps
        self._dt_s = 1.0 / self._fps
        # testworld
        if testbed_settings is None:
            testbed_settings = dict()
        self.testbed_settings = testbed_settings
        self.testbed_cls = testbed_cls
        self.testbed = None
        # debug_draw
        self.canvas = pyjs.js.document.getElementById("myCanvas")
        self.canvas.width = self.resolution[0]
        self.canvas.height = self.resolution[1]

        self.js_canvas_debug_draw = pyjs.js.canvas_debug_draw

        self.debug_draw = HtmlCanvasBatchDebugDraw(
            canvas=self.canvas, js_canvas_debug_draw=self.js_canvas_debug_draw
        )
        self.flip_bit = False

        # canvas _events THIS IS A MEM LEAK!
        js_py_mouse_up, _ = make_js_func(self.on_mouse_up)
        js_py_mouse_down, _ = make_js_func(self.on_mouse_down)
        js_py_mouse_move, _ = make_js_func(self.on_mouse_move)
        js_py_mouse_wheel, _ = make_js_func(self.on_mouse_wheel)

        js_py_touch_up, _ = make_js_func(self.on_touch_up)
        js_py_touch_down, _ = make_js_func(self.on_touch_down)
        js_py_touch_move, _ = make_js_func(self.on_touch_move)

        self.canvas["onmousedown"] = js_py_mouse_down
        self.canvas["onmousemove"] = js_py_mouse_move
        self.canvas["onmouseup"] = js_py_mouse_up


        self.canvas["ontouchstart"] =  js_py_touch_down
        self.canvas["ontouchmove"] =  js_py_touch_move
        self.canvas["ontouchend"] =  js_py_touch_up


        js_dict = pyjs.js.Function("return { passive: false }")()
        self.canvas.addEventListener("wheel", js_py_mouse_wheel, js_dict)

        # todo!
        self._debug_draw_flags = self.settings.get_debug_draw_flags()

        # flag to stop loop
        self._stop = False

        self.scale = settings.scale
        self.translate = settings.translate

        self.paused = False
        self.reached_end = False

        self._last_screen_pos = None
        self._mouse_is_down = False


    def _terminate(self):
        if not self._stop:
            self._stop = True

    def make_testbed(self):

        if self.testbed is not None:
            self.testbed.say_goodbye_world()

        self.testbed = self.testbed_cls(settings=self.testbed_settings)

        self.debug_draw.scale = self.scale

        self.debug_draw.translate = self.translate

        self.debug_draw.flip_y = True

        self.testbed.set_debug_draw(self.debug_draw)

    def _get_xy(self, e):
        boundings = self.canvas.getBoundingClientRect()
        top_left = boundings.left, boundings.top
        x = e.x - top_left[0]
        y = e.y - top_left[1]
        return x, y

    def stop(self):
        self._stop = True
        self._clear_canvas()

    def set_pause(self, p):
        self.paused = p

    def on_mouse_wheel(self, e):
        e.preventDefault()
        dy = e.deltaY
        z = self.debug_draw.scale
        if dy < 0:
            self.debug_draw.scale *= 1.1
        elif dy > 0:
            self.debug_draw.scale *= 0.9

    def on_mouse_down(self, e):
        if not self.paused:
            xpos, ypos = self._get_xy(e)
            self._mouse_is_down = True
            self._last_screen_pos = xpos, ypos

            pos = self.debug_draw.screen_to_world(self._last_screen_pos)

            pos = pos.x, pos.y

            self.testbed.on_mouse_down(pos)
    # moue callbacks
    def on_mouse_up(self, e):
        if not self.paused:

            xpos, ypos = self._get_xy(e)
            self._mouse_is_down = False
            self._last_screen_pos = xpos, ypos
            pos = self.debug_draw.screen_to_world((xpos, ypos))
            pos = pos.x, pos.y

            self.testbed.on_mouse_up(pos)

    def on_mouse_move(self, e):
        if not self.paused:
            xpos, ypos = self._get_xy(e)

            pos = self.debug_draw.screen_to_world((xpos, ypos))
            pos = pos.x, pos.y

            handled_event = self.testbed.on_mouse_move(pos)
            if (
                not handled_event
                and self._mouse_is_down
                and self._last_screen_pos is not None
            ):

                lxpos, lypos = self._last_screen_pos
                dx, dy = xpos - lxpos, ypos - lypos

                translate = self.debug_draw.translate
                self.debug_draw.translate = (
                    translate[0] + dx,
                    translate[1] - dy,
                )
            self._last_screen_pos = xpos, ypos


    def handle_touch_zoom(self, touches):
        l = touches.length
        if l < 2:
            self._last_delta = None
        else:

            t0 = e.touches[0]
            t1 = e.touches[1]
            x0,y0 = t0.clientX,t0.clientY
            x1,y1 = t1.clientX,t1.clientY

            diff = (x0 - x1)**2 + (y0 - y1)**2
            if diff > 0:
                if self._last_diff is not None:
                    q = diff / self._last_diff
                    self.debug_draw.scale *= q
                self._last_diff = diff
            else:
                self._last_diff = None

    def on_touch_down(self, e):

        e.preventDefault()
        # pyjs.js.console.log("touch down",e.touches.length)
        self.handle_touch_zoom(e.touches)
        touch = PseudoMouseEvent(e.touches[0])
        self.on_mouse_down(touch)

    def on_touch_move(self, e):
        e.preventDefault()
        self.handle_touch_zoom(e.touches)
        touch = PseudoMouseEvent(e.touches[0])
        self.on_mouse_move(touch)

    def on_touch_up(self, e):
        self._last_diff = None
        if not self.paused:
            e.preventDefault()
            # pyjs.js.console.log("touch up",e.touches.length)
            touch = ExplicitPseudoEvent(*self._last_screen_pos)
            self.on_mouse_up(touch)




    def start_ui(self):
        return self

    async def aync_start_ui(self, context):

        # make the world
        self.make_testbed()

        await self._loop()

    async def _loop(self):
        if self.reached_end:
            self.reached_end = False
        i = 0
        while not self._stop:
            i += 1
            if not self.paused:
                t0 = time.time()
                self._single_step()
                t1 = time.time()
                delta = t1 - t0
                if delta < self._dt_s:
                    timeout = self._dt_s - delta
                else:
                    timeout = 0.0001
                await asyncio.sleep(timeout)
            else:
                await asyncio.sleep(self._dt_s)

        self.reached_end = True

    def _clear_canvas(self):
        ctx = self.debug_draw.context
        canvas = self.canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        ctx.fillStyle = "black"
        ctx.fillRect(0, 0, canvas.width, canvas.height)

    def _single_step(self):

        self._clear_canvas()
        self._step_world()

    def _step_world(self):
        self.testbed.step(self._dt_s)



def gui_settings_from_context(context, **kwargs):
    gui_settings = CanvasAsyncGui.Settings.parse_obj(pyjs.to_py(context.gui_settings))
    for k,v in kwargs.items():
        setattr(gui_settings, k, v)
    return gui_settings

# hack hack things...do not change to much here =)
backends = [None]

async def run_example(testbed_cls, gui_settings, context):
    ui = b2d.testbed.run(
        testbed_cls, backend=CanvasAsyncGui, gui_settings=gui_settings
    )
    backends[0] = ui
    await ui.aync_start_ui(context)
