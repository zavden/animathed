from imports import *

ASPECT_RATIO = WIDTH / HEIGHT
FRAME_HEIGHT = 8
FRAME_WIDTH  = FRAME_HEIGHT * ASPECT_RATIO

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
  # grid
  # vertical lines
  for i in range(-7,8):
    ctx.move_to(i, 4)
    ctx.line_to(i,-4)
    ctx.set_line_width(0.03)
    if i != 0:
      ctx.set_source_rgb(0,0,0)
    else:
      ctx.set_source_rgb(*rgb(255, 0, 0))
    ctx.stroke()
  # horizontal lines
  for i in range(-4,5):
    ctx.move_to(-7, i)
    ctx.line_to( 7, i)
    ctx.set_line_width(0.03)
    if i != 0:
      ctx.set_source_rgb(0,0,0)
    else:
      ctx.set_source_rgb(*rgb(0, 0, 255))
    ctx.stroke()
  # circle at coord (2,3)
  ctx.arc(2, 3, 0.1, 0, 2 * PI)
  ctx.set_source_rgb(0,0,0)
  ctx.fill()

  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)