import tkinter as tk
from Who_is_it import find_face_def
from video_module import Video_Class, is_known_name
from config import *

os.makedirs(ROOT_DIR+"/face_and_voice/", exist_ok=True)
os.makedirs(ROOT_DIR+"/temp_img/", exist_ok=True)

Video_cap = Video_Class()

class GuiClass:
    def __init__(self, main):
        # build GUI frame
        self.main = main
        self.frame = tk.Frame(self.main)
        self.main.title("Control panel")
        self.main.geometry(panel_size)

        # add buttons - find face and add new face
        self.Find_face_btn = tk.Button(self.main, text="Who is it?", command=self.find_face_gui)
        self.Find_face_btn.pack(side=tk.TOP)
        self.add_new_face_btn = tk.Button(self.main, text=" Add new face ", command=self.add_new_face_def)
        self.add_new_face_btn.pack(side=tk.TOP)

        # add comment for the user
        self.name_face = tk.Entry(self.main)
        self.name_face.pack()
        self.label_info = tk.Label(self.main, text="")
        self.label_info.pack()
    
    # call find face function from button
    def find_face_gui(self):
        Video_cap.find_face_def()

    # call add face function from button   
    def add_new_face_def(self):
        name = self.name_face.get().lower()
        # make sure input is valid
        if name != "" and name.replace(" ", "").isalpha() and not is_known_name(name):
            self.label_info['text'] = Video_cap.add_face(name)
        else:
            self.label_info['text'] = "Name is invalid - name should be only letters or name in used - Choose a different name "
        

root = tk.Tk()
GUI = GuiClass(root)
root.mainloop()
