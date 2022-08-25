import pyjs
import b2d


class HtmlCanvasBatchDebugDraw(b2d.batch_debug_draw_cls(False, False, True)):
    def __init__(self, canvas, js_canvas_debug_draw, flags=None):
        super(HtmlCanvasBatchDebugDraw, self).__init__()
        self.canvas = canvas
        self.context = canvas.getContext("2d")
        self.js_canvas_debug_draw = js_canvas_debug_draw

        # what is drawn
        if True or flags is None:
            flags = [
                "shape",
                "joint",
                "particle",
            ]  # ,'aabb','pair','center_of_mass','particle']
        self.flags = flags
        self.clear_flags(
            ["shape", "joint", "aabb", "pair", "center_of_mass", "particle"]
        )
        for flag in flags:
            self.append_flags(flag)

    def _draw_solid_polygons(self, points, sizes, colors):
        
        js_points = pyjs.buffer_to_js_typed_array(points.ravel())
        js_sizes = pyjs.buffer_to_js_typed_array(sizes)
        js_colors = pyjs.buffer_to_js_typed_array(colors.ravel())

        self.js_canvas_debug_draw.draw_polygons(js_points, js_sizes, js_colors, True)

    def _draw_polygons(self, points, sizes, colors):
        
        js_points = pyjs.buffer_to_js_typed_array(points.ravel())
        js_sizes = pyjs.buffer_to_js_typed_array(sizes)
        js_colors = pyjs.buffer_to_js_typed_array(colors.ravel())

        self.js_canvas_debug_draw.draw_polygons(js_points, js_sizes, js_colors, False)

    def _draw_solid_circles(self, centers, radii, axis, colors):
        
        js_centers = pyjs.buffer_to_js_typed_array(centers.ravel())
        js_radii = pyjs.buffer_to_js_typed_array(radii)
        js_axis = pyjs.buffer_to_js_typed_array(axis.ravel())
        js_colors = pyjs.buffer_to_js_typed_array(colors.ravel())

        self.js_canvas_debug_draw.draw_solid_circles(
            js_centers, js_radii, js_axis, js_colors
        )

    def _draw_circles(self, centers, radii, colors):
        
        js_centers = pyjs.buffer_to_js_typed_array(centers.ravel())
        js_radii = pyjs.buffer_to_js_typed_array(radii)
        js_colors = pyjs.buffer_to_js_typed_array(colors.ravel())

        self.js_canvas_debug_draw.draw_circles(js_centers, js_radii, js_colors)

    def _draw_points(self, centers, sizes, colors):
        return

    def _draw_segments(self, points, colors):
        js_points = pyjs.buffer_to_js_typed_array(points.ravel())
        js_colors = pyjs.buffer_to_js_typed_array(colors.ravel())
        self.js_canvas_debug_draw.draw_segments(js_points, js_colors)

    def _draw_particles(self, centers, radius, colors=None):
        js_centers = pyjs.buffer_to_js_typed_array(centers.ravel())
        if colors is not None:
            colors = numpy.require(colors, dtype='uint8')

            js_colors = pyjs.buffer_to_js_typed_array(colors.ravel())
            self.js_canvas_debug_draw.draw_particles(js_centers, radius, js_colors)
        else:
            self.js_canvas_debug_draw.draw_particles(js_centers, radius)

    # non-batch api
    def draw_solid_circle(self, center, radius, axis, color):
        
        # print("draw_solid_circle")
        center = self.world_to_screen(center)
        radius = self.world_to_screen_scale(radius)
        center = numpy.require(center,dtype='uint32')
        axis = numpy.require(axis, dtype='float32')
        color = (numpy.require(color) * 255.0).astype("uint8")

        js_center = pyjs.buffer_to_js_typed_array(center.ravel())
        js_axis = pyjs.buffer_to_js_typed_array(axis.ravel())
        js_color = pyjs.buffer_to_js_typed_array(color.ravel())

        self.js_canvas_debug_draw.draw_circle_impl(js_center, radius, js_color, js_axis)

    def draw_circle(self, center, radius, color, line_width=1):
        
        center = self.world_to_screen(center)
        radius = self.world_to_screen_scale(radius)
        center = numpy.require(center, dtype='uint32')
        color = (numpy.require(color) * 255.0).astype("uint8")

        js_center = pyjs.buffer_to_js_typed_array(center.ravel())
        js_color = pyjs.buffer_to_js_typed_array(color.ravel())

        self.js_canvas_debug_draw.draw_circle_impl(js_center, radius, js_color)

    def draw_segment(self, p1, p2, color, line_width=1):
        p1 = pyjs.buffer_to_js_typed_array(numpy.require(self.world_to_screen(p1)))
        p2 = pyjs.buffer_to_js_typed_array(numpy.require(self.world_to_screen(p2)))
        color = (numpy.require(color) * 255.0).astype("uint8")
        js_color = pyjs.buffer_to_js_typed_array(color.ravel())
        self.js_canvas_debug_draw.draw_segment(
            p1, p2, js_color, self.world_to_screen_scale(line_width)
        )

    def draw_polygon(self, vertices, color, line_width=1):
        for i, ver in enumerate(vertices):
            vertices[i] = self.world_to_screen(ver)
        color = (numpy.require(color) * 255.0).astype("uint8")

        js_points = pyjs.buffer_to_js_typed_array(vertices.ravel())
        js_color = pyjs.buffer_to_js_typed_array(color.ravel())

        self.js_canvas_debug_draw.draw_poly_impl(
            int(vertices.shape[0]),
            js_points,
            js_color,
            False,
            self.world_to_screen_scale(line_width),
        )

    def draw_solid_polygon(self, vertices, color):
        for i, ver in enumerate(vertices):
            vertices[i] = self.world_to_screen(ver)
        color = (numpy.require(color) * 255.0).astype("uint8")

        js_points = pyjs.buffer_to_js_typed_array(vertices.ravel())
        js_color = pyjs.buffer_to_js_typed_array(color.ravel())

        self.js_canvas_debug_draw.draw_poly_impl(
            int(vertices.shape[0]), js_points, js_color, True
        )
