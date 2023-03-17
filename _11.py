from imports import *

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)
  # ctx.scale(WIDTH, HEIGHT)
  ctx.set_matrix(
    cairo.Matrix(
      WIDTH, 0,
      0    , HEIGHT,
      0    , 0
    )
  )

  ctx.move_to(0,0)
  ctx.line_to(0,0.1)
  ctx.move_to(0,0)
  ctx.line_to(0.1,0)

  ctx.set_line_width(0.01)
  ctx.set_source_rgba(*rgb(0, 0, 255), 1)
  ctx.stroke()

  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)
