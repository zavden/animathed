use std::io::Write;
use std::process::{Command, Stdio};
use kdam::tqdm;
use rand::random;

fn get_random_u8(width: i32, height: i32) -> Vec<u8> {
    return (0..width * height).map(|_| { random::<u8>() }).collect();
}

fn main() {
    let n_frames = 300;
    let width = 300;
    let height = 300;
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
          "./videos/_01_random_vectors.mp4",
        ])
        .stdin(Stdio::piped())
        .spawn()
        .unwrap();

    let k = child.stdin.as_mut().unwrap();
    
    for _ in tqdm!(0..n_frames) {
        k.write( &get_random_u8(width, height) ).unwrap();
    }
    child.wait().unwrap();
}


