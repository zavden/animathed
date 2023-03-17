from imports import *

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)

  ctx.arc(
    WIDTH / 2,  # x coord
    HEIGHT / 2, # y coord
    HEIGHT / 5, # radius
    0,          # start angle
    2 * PI      # end angle
  )

  ctx.set_line_width(20)
  ctx.set_source_rgba(*rgb(0, 0, 255), 1)
  ctx.stroke()
  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)

