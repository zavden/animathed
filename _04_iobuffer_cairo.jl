using Cairo

# from: https://github.com/JuliaGraphics/Cairo.jl/pull/343/files
function image_surface_get_data(surface::CairoSurface{T}) where {T}
  return ccall(
    (:cairo_image_surface_get_data, Cairo.libcairo),
    Ptr{T}, (Ptr{Nothing},), surface.ptr)
end

WIDTH  = 600
HEIGHT = 600
FPS    = 30
N_FRAMES = 150
global_buffer = IOBuffer()

function get_frame(t)
  c  = CairoRGBSurface(WIDTH, HEIGHT)
  cr = CairoContext(c)
  set_source_rgba(
    cr,
    0, 0, 1,
    t / N_FRAMES
  )
  rectangle(cr, 0, 0, WIDTH/3, HEIGHT/3)
  fill(cr)
  # Make frame
  c_data_pointer = image_surface_get_data(c)
  return unsafe_wrap(Vector{UInt32}, c_data_pointer, WIDTH * HEIGHT)
end

# Create frames
for i = 0:N_FRAMES
  write(global_buffer, get_frame(i))
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
  "./videos/iobuffer_cairo.mp4",
]

seekstart(global_buffer)
run(pipeline(global_buffer, `$command`))
