package main

import (
	"fmt"
	"os/exec"
	"github.com/ungerik/go-cairo"
  "github.com/schollz/progressbar/v3"
)

func get_frame(t int, n_frames int, width int, height int) []byte {
	surface := cairo.NewSurface(cairo.FORMAT_ARGB32, width, height)
  surface.SetSourceRGBA(0 , 0, 1, float64(t) / float64(n_frames))
  surface.Rectangle(0, 0, float64(width)/3, float64(height)/3)
  surface.Fill()
  data := surface.GetData()
	surface.Finish()
  return data
}

func main() {
  WIDTH  := 800
  HEIGHT := 800
  FPS    := 30
  N_FRAMES := 900
  bar := progressbar.Default(int64(N_FRAMES))

  cmd := exec.Command(
    "ffmpeg",
    "-y",
    "-f",
    "rawvideo",
    "-s", fmt.Sprintf("%vx%v", WIDTH, HEIGHT),
    "-pix_fmt", "rgba",
    "-r", fmt.Sprintf("%v", FPS),
    "-i",
    "-",
    "-loglevel", "error",
    "-vcodec", "libx264", "-pix_fmt", "yuv420p",
    "./videos/out_cairo.mp4",
  )
  si, _ := cmd.StdinPipe()

  cmd.Start()
  for i := 0; i <= N_FRAMES; i++ {
    si.Write(get_frame(i, N_FRAMES, WIDTH, HEIGHT))
    bar.Add(1)
  }
  si.Close()
  cmd.Wait()
}
