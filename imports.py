import cairo
import subprocess, os, platform, sys
import numpy as np
from math import pi as PI

WIDTH  = 1920
HEIGHT = 1080
TMP_PATH = "./outputs/tmp.png"

FRAME_ARGS = [
  cairo.FORMAT_ARGB32, WIDTH, HEIGHT
]

def rgb(r,g,b):
  """From normalized to 255 scale"""
  return [r/255, g/255, b/255]

def save_and_open_image(file, draw_frame):
  img       = draw_frame()
  file_name = os.path.basename(file)[:-3] + ".png"
  path      = f"./outputs/{file_name}"
  # INFO: Save the file with the name
  # _file_number.png 
  # and also in tmp.png to open it
  img.write_to_png(path)
  img.write_to_png(TMP_PATH)
  # INFO: Open file with preview flag
  if "--preview" in sys.argv:
    if platform.system() == 'Darwin':       # macOS
      subprocess.Popen(('open', TMP_PATH))
    elif platform.system() == 'Windows':    # Windows
      os.startfile(TMP_PATH)
    else:                                   # linux variants
      subprocess.Popen(('xdg-open', TMP_PATH))
