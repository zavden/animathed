using Cairo
using ProgressBars

# from: https://github.com/JuliaGraphics/Cairo.jl/pull/343/files
function image_surface_get_data(surface::CairoSurface{T}) where {T}
  return ccall(
    (:cairo_image_surface_get_data, Cairo.libcairo),
    Ptr{T}, (Ptr{Nothing},), surface.ptr)
end

WIDTH  = 1000
HEIGHT = 1000
FPS    = 60
N_FRAMES = 1200

function get_frame(t)
  c  = CairoRGBSurface(WIDTH, HEIGHT)
  cr = CairoContext(c)
  set_source_rgba(cr, 0, 0, 1, t / N_FRAMES)
  rectangle(cr, 0, 0, WIDTH/3, HEIGHT/3)
  fill(cr)
  # Make frame
  c_data_pointer = image_surface_get_data(c)
  frame = unsafe_wrap(Vector{UInt32}, c_data_pointer, WIDTH * HEIGHT)
  return [frame, c]
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
  "./videos/_06_pipe_cairo.mp4",
]

stdin_PIPE = Pipe()
proc = run(pipeline(`$command`, stdin=stdin_PIPE), wait=false)

for i = tqdm(0:N_FRAMES)
  frame, c = get_frame(i)
  write(stdin_PIPE, frame)
  Cairo.finish(c) # <- Clean cairo buffer
end

close(stdin_PIPE)
wait(proc)
