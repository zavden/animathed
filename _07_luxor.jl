using Luxor, ProgressBars

WIDTH    = 600
HEIGHT   = 600
N_FRAMES = 100
FPS = 10

# from: https://github.com/JuliaGraphics/Cairo.jl/pull/343/files
function image_surface_get_data(surface::Luxor.Cairo.CairoSurface{T}) where {T}
  return ccall(
    (:cairo_image_surface_get_data, Luxor.Cairo.libcairo),
    Ptr{T}, (Ptr{Nothing},), surface.ptr)
end

function get_frame(t)
  cd = Drawing(WIDTH, HEIGHT)
  rotate((t / N_FRAMES) * 2π)
  juliacircles(100)

  c_data_pointer = image_surface_get_data(cd.surface)
  frame = unsafe_wrap(Vector{UInt32}, c_data_pointer, WIDTH * HEIGHT)
  finish()
  return frame
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
  "./videos/_07_luxor.mp4",
]

stdin_PIPE = Pipe()
proc = run(pipeline(`$command`, stdin=stdin_PIPE), wait=false)

for i = tqdm(1:N_FRAMES)
  frame = get_frame(i)
  write(stdin_PIPE, frame)
end

close(stdin_PIPE)
wait(proc)
