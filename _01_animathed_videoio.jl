# From: https://juliaio.github.io/VideoIO.jl/stable/writing/#Iterative-Encoding
using VideoIO

WIDTH  = 300
HEIGHT = 300
FPS    = 30
N_FRAMES = 200

frames = map(x->rand(UInt8, WIDTH, HEIGHT), 1:N_FRAMES) # vector of 2D arrays

open_video_out("./videos/out1.mp4", frames[1], framerate=FPS) do movie
  for frame in frames
    write(movie, frame)
  end
end
