import face_recognition
from os import path, remove
from shutil import copy
import glob
import vlc
from gtts import gTTS
import time
from config import ROOT_DIR,TEMP_DIR,LOAD_DIR, Without_voice_announcement
import numpy as np

class RecognitionClass:
    def __init__(self):
        
        # Load known pictures
        self.update_known_faces()

    def update_known_faces(self):
        self.known_face_names = []
        self.known_face_encodings = []
        for img_path in glob.glob(LOAD_DIR+"/*.jpg"):
            filename = path.split(img_path)[-1]
            # check if voice file exists
            if path.exists(LOAD_DIR+"/"+filename[:-4]+".mp3"):
                image = face_recognition.load_image_file(img_path)
                face_encoding_data = face_recognition.face_encodings(image)
                if face_encoding_data==[]:
                    remove(LOAD_DIR+"/"+filename[:-4]+".jpg")
                    remove(LOAD_DIR+"/"+filename[:-4]+".mp3")
                else:
                    self.known_face_names.append(filename[:-4])
                    self.known_face_encodings.append(face_encoding_data[0])

    def recognition(self, rgb_small_frame):
        """
        Returns two arrays  
        1.bounding boxes of human faces in a image
        2.face encoded 
        """
        # Find all the faces in current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        return face_locations, face_encodings
    
    def matching(self, face_encodings):
        """
        Returns matching faces
        """
        face_names = []
        
        for face_encoding in face_encodings:
            name = "Unknown"
            # check if the face is a match for the known faces
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            if matches == []:
                face_names.append(name)
                return face_names

            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)
        return face_names
    
    def find_faces_and_match(self, rgb_small_frame):
        """
        Returns two arrays  
        1.bounding boxes of human faces in a image
        2.names of each human
        """
        face_locations, face_encodings = self.recognition(rgb_small_frame)
        face_names = self.matching(face_encodings)
        
        return face_locations, face_names

    def voice_announcement(self, name):
        """
        Announcing the name
        """
        if Without_voice_announcement:
            return
        player = vlc.MediaPlayer(LOAD_DIR+"/"+name+".mp3")
        player.play()

        time.sleep(1.5)
        duration = player.get_length() / 1000
        time.sleep(duration)
        return

    def add_face_and_voice(self, name):
        """ add face and voice to the known group"""
        # add picture 
        if path.exists(TEMP_DIR+"/temp.jpg"):
            copy(TEMP_DIR+"/temp.jpg", LOAD_DIR+"/"+name+".jpg")
        # add voice
        text_to_speech = "Hello "+name
        speech = gTTS(text=text_to_speech, lang="en", slow=False)
        speech.save(LOAD_DIR+"/"+name+".mp3")

        return 

    def is_face_encoded(self,rgb_small_frame):
        """ return bool if face encoded """
        face_locations, face_encodings = self.recognition(rgb_small_frame)
        if face_encodings==[]:
            return False
        return True