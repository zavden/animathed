from imports import *

ASPECT_RATIO = WIDTH / HEIGHT # 16/9
# Manim units
FRAME_HEIGHT = 8
FRAME_WIDTH  = ASPECT_RATIO * FRAME_HEIGHT

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)
  ctx.set_matrix(
    cairo.Matrix(
      WIDTH / FRAME_WIDTH, 0,
      0                  , - HEIGHT / FRAME_HEIGHT,
      WIDTH / 2          , HEIGHT / 2,
    )
  )
  # x line
  ctx.move_to(0,0)
  ctx.line_to(1,0)
  ctx.set_line_width(0.08)
  ctx.set_source_rgba(*rgb(255, 0, 0), 1)
  ctx.stroke()
  # y line
  ctx.move_to(0,0)
  ctx.line_to(0,1)
  ctx.set_line_width(0.08)
  ctx.set_source_rgba(*rgb(0, 0, 255), 1)
  ctx.stroke()
  # rect
  ctx.rectangle(0, 0, 1, 1)
  ctx.set_source_rgba(*rgb(0, 255, 0), 0.5)
  ctx.fill()

  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)
