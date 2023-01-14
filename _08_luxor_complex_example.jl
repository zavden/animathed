using Luxor, ProgressBars

WIDTH  = 1920
HEIGHT = 1080
TOTAL_TIME = 18 # seconds
FPS = 60
N_FRAMES = TOTAL_TIME * FPS

dt = 1 / FPS

# from: https://github.com/JuliaGraphics/Cairo.jl/pull/343/files
function image_surface_get_data(surface::Luxor.Cairo.CairoSurface{T}) where {T}
  return ccall(
    (:cairo_image_surface_get_data, Luxor.Cairo.libcairo),
    Ptr{T}, (Ptr{Nothing},), surface.ptr)
end

# http://juliagraphics.github.io/Luxor.jl/stable/howto/clipping/
function get_frame(t)
  cd = Drawing(WIDTH, HEIGHT, :image)
  origin()
  s = hypotrochoid(400, 48, 88, vertices=true)
  setline(0.5)
  sethue("grey60")
  poly(s, :stroke)
  c = box(O, 350 + t * dt * 30, 350 + t * dt * 30)
  poly(c, :stroke, close=true)
  sethue("gold")
  setline(2)
  poly(polyclip(s, c), :stroke, close=true)

  c_data_pointer = image_surface_get_data(cd.surface)
  frame = unsafe_wrap(Vector{UInt32}, c_data_pointer, WIDTH * HEIGHT)
  return [frame, cd.surface]
end

# print(get_frame())

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
  "./videos/_08_luxor_complex_exaple.mp4",
]

stdin_PIPE = Pipe()
proc = run(pipeline(`$command`, stdin=stdin_PIPE), wait=false)

for i = tqdm(1:N_FRAMES)
  frame, c = get_frame(i)
  write(stdin_PIPE, frame)
  Luxor.Cairo.finish(c)
end

close(stdin_PIPE)
wait(proc)
