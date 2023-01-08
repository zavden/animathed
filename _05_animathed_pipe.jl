WIDTH  = 600
HEIGHT = 600
FPS    = 30
N_FRAMES = 150
img = rand(UInt8, WIDTH * HEIGHT * 4)

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
  "./videos/out5.mp4",
]

stdin_PIPE = Pipe()
proc = run(pipeline(`$command`, stdin=stdin_PIPE), wait=false)

for i = 0:N_FRAMES
  write(stdin_PIPE, img)
  # write(stdin_PIPE, rand(UInt8, WIDTH * HEIGHT * 4))
end

close(stdin_PIPE)
wait(proc)
