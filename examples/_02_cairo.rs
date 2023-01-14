use std::io::Write;
use std::process::{Command, Stdio};
use cairo::ImageSurfaceDataOwned;
use kdam::tqdm;
use cairo::ImageSurface;
use cairo::Format::ARgb32;
use cairo::Context;


fn get_frame(
    t: i32, n_frames: i32, width: i32, height: i32
  ) -> ImageSurfaceDataOwned {
    let img_surface = ImageSurface::create(ARgb32, width, height).unwrap();
    let img_ctx = Context::new(&img_surface).unwrap();
    img_ctx.set_source_rgba(1.0, 0.0, 1.0, f64::from(t) / f64::from(n_frames));
    img_ctx.rectangle(0.0, 0.0, f64::from(width)/3.0, f64::from(height)/3.0);
    img_ctx.fill().unwrap();
    
    drop(img_ctx); // https://github.com/gtk-rs/cairo/issues/278#issuecomment-520709671
    return img_surface.take_data().unwrap();
}


fn main() {
    let width    = 800;
    let height   = 800;
    let n_frames = 900;
    let fps = 30;

    let mut child = Command::new("ffmpeg")
        .args([
          "-y",
          "-f",
          "rawvideo",
          "-s", &format!("{}x{}", width, height),
          "-pix_fmt", "rgba",
          "-r", &format!("{}", fps),
          "-i",
          "-",
          "-loglevel","error",
          "-vcodec", "libx264", "-pix_fmt", "yuv420p",
          "./videos/_02_cairo.mp4",
        ])
        .stdin(Stdio::piped())
        .spawn()
        .unwrap();

    let k = child.stdin.as_mut().unwrap();
    
    for t in tqdm!(0..n_frames) {
        let surface = get_frame(t, n_frames, width, height);
        k.write( surface.as_ref() ).unwrap();
    }
    child.wait().unwrap();
}

