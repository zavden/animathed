import subprocess as sp
import progressbar
import os
import platform


def make_frame(draw_frame_func, t, width, height):
    """
    Convert cairo.ImageSurface to RAW (bytes) data
    """
    frame = draw_frame_func(t, width, height)
    data = frame.get_data().tobytes()
    return data

def open_file(file_path):
    """
    Open video file at the end
    """
    current_os = platform.system()

    if current_os == "Windows":
        os.startfile(file_path)
    else:
        commands = []
        if current_os == "Linux":
            commands.append("xdg-open")
        elif current_os.startswith("CYGWIN"):
            commands.append("cygstart")
        else:  # Assume macOS
            commands.append("open")

        commands.append(file_path)

        sp.call(commands, stderr=sp.STDOUT)


def run(draw_frame_func, total_frames, output_name, width=500, height=500, frame_rate=30):
    # total_frames += 1
    command = [
        'ffmpeg',
        '-y', # replace the video if it already exists
        '-f',
        'rawvideo', # input data: bytes
        '-s', '%dx%d' % (width, height),
        '-pix_fmt', 'rgba',
        '-r', str(frame_rate),
        '-i',
        '-', # pipe input
        '-loglevel','error',
        '-vcodec', 'libx264', '-pix_fmt', 'yuv420p',
        f'videos/{output_name}.mp4' # output
    ]

    p = sp.Popen(command, stdin=sp.PIPE)
    bar = progressbar.ProgressBar(maxval=total_frames).start()

    for t in range(total_frames):
        data = make_frame(draw_frame_func, t, width, height)
        p.stdin.write(data) # add image raw to the buffer
        bar.update(t)
    p.stdin.close()
    p.wait()
    open_file(f"videos/{output_name}.mp4")


