from imports import *

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)
  # ctx.scale(WIDTH, HEIGHT)

  ctx.rectangle(
      #  x pos , y pos
      WIDTH / 2, HEIGHT / 2,
      #  width , height
      WIDTH / 2, HEIGHT / 2
  )

  ctx.set_line_width(50)
  ctx.set_source_rgba(*rgb(0, 0, 255), 1)
  ctx.stroke()
  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)
