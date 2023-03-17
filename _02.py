from imports import *

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)

  ctx.move_to(0, 0)
  ctx.line_to(0, 500)

  ctx.line_to(500, 500)
  ctx.line_to(500, 0)
  ctx.close_path()

  ctx.set_line_width(20)
  ctx.set_source_rgba(*rgb(0, 0, 255), 1)
  ctx.stroke()

  return surface


if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)
