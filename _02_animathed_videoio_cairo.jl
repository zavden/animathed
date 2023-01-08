using VideoIO
using Cairo
using FileIO

WIDTH  = 600
HEIGHT = 600
FPS    = 30
N_FRAMES = 1000

function get_frame(t)
  c  = CairoRGBSurface(WIDTH, HEIGHT)
  cr = CairoContext(c)
  buffer = IOBuffer()
  set_source_rgba(
    cr,
    0, 0, 1,
    t / N_FRAMES
  )
  rectangle(cr, 0, 0, WIDTH/3, HEIGHT/3)
  fill(cr);
  write_to_png(c, buffer)
  return load(buffer)
end

open_video_out("./videos/out2.mp4", get_frame(0), framerate=FPS) do movie
  for i in 1:N_FRAMES
    write(movie, get_frame(i))
  end
end

