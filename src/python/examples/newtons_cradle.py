from b2d.testbed import TestbedBase
import random
import numpy
import b2d
import math
import random


class NewtonsCradle(TestbedBase):

    name = "newton's cradle"

    def __init__(self, settings=None):
        super(NewtonsCradle, self).__init__(settings=settings)

        # radius of the circles
        r = 1.0
        # length of the rope
        l = 10.0
        # how many balls
        n = 10

        offset = (l + r, 2 * r)
        dynamic_circles = []
        static_bodies = []
        for i in range(n):
            if i + 1 == n:
                position = (offset[0] + i * 2 * r + l, offset[1] + l)
            else:
                position = (offset[0] + i * 2 * r, offset[1])

            circle = self.world.create_dynamic_body(
                position=position,
                fixtures=b2d.fixture_def(
                    shape=b2d.circle_shape(radius=r * 0.90),
                    density=1.0,
                    restitution=1.0,
                    friction=0.0,
                ),
                linear_damping=0.01,
                angular_damping=1.0,
                fixed_rotation=True,
            )
            dynamic_circles.append(circle)

            static_body = self.world.create_static_body(
                position=(offset[0] + i * 2 * r, offset[1] + l)
            )

            self.world.create_distance_joint(
                static_body,
                circle,
                local_anchor_a=(0, 0),
                local_anchor_b=(0, 0),
                max_length=l,
                stiffness=0,
            )

            static_bodies.append(static_body)


async def async_main(context):
    gui_settings = gui_settings_from_context(context)
    await run_example(NewtonsCradle, gui_settings, context)