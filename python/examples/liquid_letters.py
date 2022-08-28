"""
Color Mixing
===========================

This example show how to create particles which mix colors when they touch
"""

from b2d.testbed import TestbedBase
import random
import numpy
import b2d
import sys
import math

def get_char(c):
    if c == "A":
        return [
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
        ]
    elif c == "B":
        return [
            [1,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,0],
        ]
    elif c == "C":
        return [
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,1],
            [0,1,1,1,0],
        ]
    elif c == "D":
        return [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
    elif c == "E":
        return [
            [1,1,1,1,1],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,1],
        ]
    elif c == "F":
        return [
            [1,1,1,1,1],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
        ]
    elif c == "G":
        return [
            [0,1,1,1,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0],
        ]
    elif c == "H":
        return [
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
        ]
    elif c == "I":
        return [
            [1,1,1],
            [0,1,0],
            [0,1,0],
            [0,1,0],
            [0,1,0],
            [0,1,0],
            [1,1,1],
        ]
    elif c == "J":
        return [
            [0,0,0,1],
            [0,0,0,1],
            [0,0,0,1],
            [0,0,0,1],
            [0,0,0,1],
            [1,0,0,1],
            [0,1,1,0],
        ]
    elif c == "K":
        return [
            [1,0,0,0,1],
            [1,0,0,1,0],
            [1,0,1,0,0],
            [1,1,0,0,0],
            [1,0,1,0,0],
            [1,0,0,1,0],
            [1,0,0,0,1],
        ]
    elif c == "L":
        return [
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,1],
        ]
    elif c == "M":
        return [
            [1,0,0,0,1],
            [1,1,0,1,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
        ]
    elif c == "N":
        return [
            [1,0,0,0,1],
            [1,1,0,0,1],
            [1,0,1,0,1],
            [1,0,0,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
        ]
    elif c == "O":
        return [
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0],
        ]
    elif c == "P":
        return [
            [1,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
        ]
    elif c == "Q":
        return [
            [0,1,1,1,0,0],
            [1,0,0,0,1,0],
            [1,0,0,0,1,0],
            [1,0,0,0,1,0],
            [1,0,0,0,1,0],
            [1,0,0,0,1,0],
            [0,1,1,1,1,1],
        ]
    elif c == "R":
        return [
            [1,1,1,1,0],
            [1,0,0,0,1],
            [1,1,1,1,0],
            [1,0,1,0,0],
            [1,0,0,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
        ]
    elif c == "S":
        return [
            [0,1,1,1,1],
            [1,0,0,0,0],
            [0,1,1,1,0],
            [0,0,0,0,1],
            [0,0,0,0,1],
            [0,0,0,0,1],
            [1,1,1,1,0],
        ]
    elif c == "T":
        return [
            [1,1,1,1,1],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
        ]
    elif c == "U":
        return [
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0],
        ]
    elif c == "V":
        return [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
    elif c == "W":
        return [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
    elif c == "X":
        return [
            [1,0,0,0,1],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
        ]
    elif c == "Y":
        return [
            [1,0,0,0,1],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
        ]
    elif c == "Z":
        return [
            [1,1,1,1,1],
            [0,0,0,0,1],
            [0,0,0,0,1],
            [0,0,0,1,0],
            [0,0,1,0,0],
            [0,1,0,0,0],
            [1,1,1,1,1],
        ]
    elif c == " ":
        return [
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]
    elif c == "-":
        return [
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [1,1,1],
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]





def shape_from_text(text, center, size=1,f=0.8):

    size = size
    all_shapes = []
    for c in text:
        letter_shapes = []
        c = numpy.fliplr(numpy.array(get_char(c)).T)
        for x in range(c.shape[0]):
            for y in range(c.shape[1]):
                if c[x,y] == 1:
                    s = b2d.polygon_shape(box=[size/2*f, size/2*f], center=(x*size + center[0], y*size + center[1]))
                    letter_shapes.append(s)
        center = (center[0] + c.shape[0]+1, center[1])
        all_shapes.append(letter_shapes)
    return all_shapes

def heart_shape(center, size):

    return [
        b2d.polygon_shape(vertices=[
            (0+center[0],0+center[1]),
            (size+center[0],size+center[1]),
            (-size+center[0],size+center[1])
        ]),
        b2d.polygon_shape(vertices=[
            (-size+center[0], size+center[1]),
            (-size/2+center[0],size*1.5+center[1]),
            (        center[0],size+center[1])
        ])
        ,
        b2d.polygon_shape(vertices=[
            (size+center[0], size+center[1]),
            (size/2+center[0],size*1.5+center[1]),
            (        center[0],size+center[1])
        ])
    ]



class Letters(TestbedBase):

    name = "Letters"

    def __init__(self, settings=None):
        super(Letters, self).__init__(settings=settings)
        dimensions = [80, 100]

        # the outer box
        box_shape = b2d.ChainShape()
        box_shape.create_loop(
            [
                (0, 0),
                (0, dimensions[1]),
                (dimensions[0], dimensions[1]),
                (dimensions[0], 0),
            ]
        )
        l = self.world.create_static_body(position=(0, 0), shape=box_shape)

        # letter = self.world.create_dynamic_body(position=(0, 0), shapes=shape_from_char('A', center=(5,5)), density=1)

        fixtureA = b2d.fixture_def(
            shape=b2d.circle_shape(2), density=2.2, friction=0.2, restitution=0.5
        )
        body = self.world.create_dynamic_body(position=(20, 55), fixtures=fixtureA)

        pdef = b2d.particle_system_def(
            viscous_strength=0.9,
            spring_strength=0.0,
            damping_strength=0.5,
            pressure_strength=0.5,
            color_mixing_strength=0.008,
            density=2,
        )
        psystem = self.world.create_particle_system(pdef)
        psystem.radius = 0.5
        psystem.damping = 1.0




        lines = [
            ([[b2d.polygon_shape(box=(dimensions[0]/2*0.9,3), center=(dimensions[0]/2,40))]], (85,170,127,255)),
            (shape_from_text('QUANT STACK', center=(5,30), size=0.8, f=0.9), (246,241,147,255)),
            ([heart_shape(size=5, center=(30,20))], (255,0,0,255)),
            (shape_from_text(' EURO-SCIPY', center=(5,10), size=0.8, f=0.9), (66,115,165,255)),
            ([[b2d.polygon_shape(box=(dimensions[0]/2*0.9,3), center=(dimensions[0]/2,5))]], (246,241,147,255)),
        ]

        for line_shapes,color in lines:
            for shapes in line_shapes:
                for shape in shapes:
                    pgDef = b2d.particle_group_def(
                        flags=b2d.ParticleFlag.waterParticle
                        | b2d.ParticleFlag.colorMixingParticle,
                        # group_flags=b2d.ParticleGroupFlag.solidParticleGroup,
                        shape=shape,
                        strength=1.0,
                        color=color,
                    )
                    group = psystem.create_particle_group(pgDef)


async def async_main(context):
    gui_settings = gui_settings_from_context(context, translate=[0,-500],scale=8)
    await run_example(Letters, gui_settings, context)