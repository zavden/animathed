from imports import *

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)

  # ctx.move_to(100, 100) # only works 
  # with lines and bezier curves

  ctx.rectangle(
  #(x, y) coord of corner UP + LEFT 
    0, 0,
  # width  , height
    WIDTH/3, HEIGHT/3
  )
  ctx.set_source_rgba(*rgb(0, 255, 0), 1)
  ctx.fill_preserve()
  # ctx.fill() # kills the path

  ctx.set_source_rgba(*rgb(0, 0, 255), 1)
  ctx.set_line_width(60)
  ctx.stroke_preserve()
  # ctx.stroke() # kills the path

  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)
