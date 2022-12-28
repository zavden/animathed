import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# read this: https://www.geeksforgeeks.org/python-import-from-parent-directory/

import animathed
import cairo
from math import pi as PI

TOTAL_FRAMES = 200
WIDTH = 800
HEIGHT = 500
FPS = 30

def color(r,g,b):
    return [b/255,g/255,r/255]

def draw_frame(t, width, height):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    RADIUS = 200

    ctx.translate(width/2, height/2)
    ctx.arc(0, 0, RADIUS, 0, 2* PI * t / TOTAL_FRAMES)
    ctx.set_source_rgb(*color(255,0,0))
    ctx.stroke()

    return surface


if __name__ == '__main__':
    animathed.run(draw_frame, TOTAL_FRAMES, "write_circle", WIDTH, HEIGHT, FPS)
