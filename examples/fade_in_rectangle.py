import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# read this: https://www.geeksforgeeks.org/python-import-from-parent-directory/

import animathed
import cairo

TOTAL_FRAMES = 200
WIDTH = 800
HEIGHT = 500
FPS = 30

def color(r, g, b):
    return [b / 255, g / 255, r / 255]

def draw_frame(t, width, height):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    # Fade in rectangle
    ctx.set_source_rgba(1, 0, 0, t/TOTAL_FRAMES)
    # ctx.set_source_rgba(*color(0,0,255), t/TOTAL_FRAMES)
    # ctx.translate(width/3, height/3)
    ctx.rectangle(0, 0, width/3, height/3)
    ctx.fill()

    return surface


if __name__ == '__main__':
    animathed.run(draw_frame, TOTAL_FRAMES, "fade_in", WIDTH, HEIGHT, FPS)


