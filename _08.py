from imports import *

def draw_frame():
  surface = cairo.ImageSurface(*FRAME_ARGS)
  ctx = cairo.Context(surface)

  m = np.array([
    [2, 1, 3],
    [5, 2, 6],
    [0, 0, 1],
  ])

  ctx.set_matrix(
    cairo.Matrix(
      m[0][0], m[0][1], # 2, 1
      m[1][0], m[1][1], # 5, 2
      m[0][2], m[1][2], # 3, 6
    )
  )
  return surface

if __name__ == '__main__':
  save_and_open_image(__file__, draw_frame)
