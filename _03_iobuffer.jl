WIDTH  = 600
HEIGHT = 600
FPS    = 30
N_FRAMES = 150

global_buffer = IOBuffer()

for i = 1:N_FRAMES
  img = rand(UInt8, WIDTH * HEIGHT * 4)
  write(global_buffer, img)
end

command = [
  "ffmpeg",
  "-y",
  "-f",
  "rawvideo",
  "-s", "$(WIDTH)x$(HEIGHT)",
  "-pix_fmt", "rgba",
  "-r","$(FPS)",
  "-i",
  "-",
  "-loglevel","error",
  "-vcodec", "libx264", "-pix_fmt","yuv420p",
  "./videos/_04_iobuffer.mp4",
]

seekstart(global_buffer)
run(pipeline(global_buffer, `$command`))

