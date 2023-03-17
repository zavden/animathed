from imports import *

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)
  ctx.scale(WIDTH, HEIGHT)

  ctx.rectangle(1/2, 1/2, 1/2, 1/2)
  # ctx.rectangle(0, 0, 1/2, 1/2)

  ctx.set_line_width(0.05)
  ctx.set_source_rgba(*rgb(0, 0, 255), 1)
  ctx.stroke()
  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)

