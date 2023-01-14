using Luxor, ProgressBars, Colors

WIDTH  = 1920
HEIGHT = 1080
TOTAL_TIME = 5 # seconds
FPS = 10
N_FRAMES = TOTAL_TIME * FPS

dt = 1 / FPS

# from: https://github.com/JuliaGraphics/Cairo.jl/pull/343/files
function image_surface_get_data(surface::Luxor.Cairo.CairoSurface{T}) where {T}
  return ccall(
    (:cairo_image_surface_get_data, Luxor.Cairo.libcairo),
    Ptr{T}, (Ptr{Nothing},), surface.ptr)
end

# http://juliagraphics.github.io/Luxor.jl/stable/tutorial/pixels/
f(z, t) = (z + 3 + t*0.05)^3 / ((z + 2im) * (z - 2im)^2)

function pixelcolor(r, c, t;
        rows = 100,
        cols = 100)
    z = rescale(r, 1, rows, -2π, 2π) + rescale(c, 2π, cols, -2π, 2π) * im
    n = f(z, t)
    h = 360rescale(angle(n), 0, 2π)
    s = abs(sin(π / 2 * real(f(z, t))))
    v = abs(sin(2π * real(f(z, t))))
    return HSV(h, s, v)
end

function get_frame(t)
  A = zeros(ARGB32, HEIGHT, WIDTH)
  Drawing(A)

  for r in 1:size(A, 1), c in 1:size(A, 2)
      A[r, c] = pixelcolor(r, c, t, rows=HEIGHT, cols=WIDTH)
  end
  finish()

  c = Drawing(WIDTH, HEIGHT, :image)
  origin()
  placeimage(A, Point(-WIDTH/2, -HEIGHT/2))

  c_data_pointer = image_surface_get_data(c.surface)
  frame = unsafe_wrap(Vector{UInt32}, c_data_pointer, WIDTH * HEIGHT)
  return [frame, c.surface]
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
  "./videos/_09_luxor_pixels.mp4",
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

