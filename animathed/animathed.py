import subprocess as sp
import progressbar
import os
import platform


def make_frame(draw_frame_func, frame_num, width, height):
    """
    Convert Cairo.ImageSurface to RAW data
    """
    frame = draw_frame_func(frame_num, width, height)
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

            FNULL = open(os.devnull, 'w')
            sp.call(commands, stdout=FNULL, stderr=sp.STDOUT)
            FNULL.close()


def run(draw_frame_func, frame_count, output_name, width=500, height=500, frame_rate=30):
    # frame_count += 1
    command = [
        'ffmpeg',
        '-y',
        '-f',
        'rawvideo',
        '-s', '%dx%d' % (width, height),
        '-pix_fmt', 'rgba',
        '-r', str(frame_rate),
        '-i', '-',
        '-loglevel','error',
        '-vcodec', 'libx264', '-pix_fmt', 'yuv420p',
        f'videos/{output_name}.mp4'
    ] 

    p = sp.Popen(command, stdin=sp.PIPE)
    bar = progressbar.ProgressBar(maxval=frame_count).start()

    for frame_num in range(frame_count):
        data = make_frame(draw_frame_func, frame_num, width, height)
        p.stdin.write(data) # add image raw to the buffer
        bar.update(frame_num)
    p.stdin.close()
    p.wait()
    open_file(f"videos/{output_name}.mp4")


