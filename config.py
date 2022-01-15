import os

from cv2 import resize
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TEMP_DIR = ROOT_DIR + "/temp_img"
LOAD_DIR = ROOT_DIR + "/face_and_voice"

panel_size = "500x100"

resize_frame = 0.25

Without_voice_announcement = False