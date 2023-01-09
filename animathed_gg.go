package main

import (
	"fmt"
  "os/exec"
  "github.com/schollz/progressbar/v3"
	"reflect"
	"github.com/fogleman/gg"
)


func get_frame(t int, n_frames int, width int, height int) []byte  {
	dc := gg.NewContext(width, height)
  dc.SetRGBA(1, 1, 0, float64(t)/float64(n_frames))
  dc.DrawRectangle(0, 0, float64(width)/3, float64(height)/3)
  dc.Fill()
  image := dc.Image()
  r := reflect.ValueOf(image)
  var f []byte = reflect.Indirect(r).FieldByName("Pix").Bytes()
  return f
}

func main() {
  WIDTH := 600
  HEIGHT := 600
  N_FRAMES := 500
  FPS := 30

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
    "./videos/out_gg.mp4",
  )
  si, _ := cmd.StdinPipe()

  cmd.Start()
  for i := 0; i <= N_FRAMES; i++ {
    si.Write(get_frame(i, N_FRAMES, WIDTH, HEIGHT))
    bar.Add(1)
  }
  si.Close()
  cmd.Wait()

	// dc.SavePNG("out.png")
}

