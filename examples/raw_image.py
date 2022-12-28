import cairo

width = 2
height = 2

surface = cairo.ImageSurface(
    cairo.FORMAT_ARGB32, width, height
)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 0, 0)
ctx.rectangle(0, 0, 1, 1)
ctx.fill()
# ctx.set_source_rgb(0, 1, 1)
# ctx.rectangle(1, 0, 1, 1)
# ctx.fill()
print(surface.get_data().tobytes())
surface.write_to_png("raw.png")
