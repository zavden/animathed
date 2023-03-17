from imports import *

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)
  rect_args = [0, 0, WIDTH / 2, HEIGHT / 2]

  ctx.rectangle(*rect_args) # Blue rect

  ctx.set_line_width(20)
  ctx.set_source_rgba(*rgb(0, 0, 255), 1)
  ctx.stroke()

  ctx.save() # <-- Save state system coords

  # Matrix equivalent to scale(2,2)
  ctx.set_matrix(
    cairo.Matrix(
      2, 0,
      0, 2,
      0, 0
    )
  )

  ctx.rectangle(*rect_args) # Red rectangle

  ctx.set_line_width(20)
  ctx.set_source_rgba(*rgb(255, 0, 0), 0.5)
  ctx.stroke()

  ctx.restore() # <-- Restore system coords

  ctx.rectangle(*rect_args) # Green rectangle

  ctx.set_source_rgba(*rgb(0, 255, 0), 0.5)
  ctx.fill()
  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)
