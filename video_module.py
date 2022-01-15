import cv2
import time
from recognition_module import RecognitionClass
from config import ROOT_DIR, resize_frame ,LOAD_DIR, TEMP_DIR
from os import path

def is_known_name(name):
        """ return bool  - name is known/unknown """
        return (path.exists(LOAD_DIR+"/"+name+".mp3")
                or path.exists(LOAD_DIR+"/"+name+".jpg")) 


class Video_Class:
    def __init__(self):
        self.reco = RecognitionClass()
        self.face_locations = []
        self.face_names = []
        

    def add_face(self,new_name):
        if self.video_stream(add_new_face=True,find_face=False):
            
            img = cv2.imread(TEMP_DIR+"/temp.jpg")
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(img, (0, 0), fx=resize_frame, fy=resize_frame)
            # Convert the image to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            self.reco.add_face_and_voice(new_name)
            cv2.destroyAllWindows()
            img = cv2.imread(LOAD_DIR+"/"+new_name+".jpg")
            cv2.imshow(new_name, img)
            self.reco.voice_announcement(new_name)
            while True:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            self.reco.update_known_faces()
            cv2.destroyAllWindows()
            return "new preson added"
        
        cv2.destroyAllWindows()
        return "capture failed"

    def find_face_def(self):
        if self.video_stream(add_new_face=False,find_face=True):
            print(self.face_names)
            for name in self.face_names:
                if name != "Unknown":
                    self.reco.voice_announcement(name)
            while True:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()

        
    def video_stream(self,add_new_face=False,find_face=False):

        # Initialize face recognition variables
        self.face_locations = []
        self.face_names = []

        # Initialize Video Capture
        videostream = cv2.VideoCapture(0)
        # Frame buffer equal to 1
        videostream.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        stop_video_flag = False
        while not stop_video_flag:
            time1 = time.time()
            # Grab frame from video stream
            ret, frame = videostream.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=resize_frame, fy=resize_frame)

            # Convert the image to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # find all faces and check if they match to known faces.
            self.face_locations, self.face_names = self.reco.find_faces_and_match(rgb_small_frame)

            # Scale back up faces and draw box around them
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # save unknown face  
                if add_new_face:
                    if name == "Unknown" and self.reco.is_face_encoded(rgb_small_frame):
                        cv2.imwrite(TEMP_DIR+"/temp.jpg", frame[top-10:bottom+10, left-10:right+10])
                        stop_video_flag = True
                
                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

            # Calculate fps
            frame_rate_calc = (1/(time.time()-time1))
            
            # Add fps
            cv2.putText(frame, 'FPS: {0:.2f}'.format(frame_rate_calc), (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)

            # add comment below
            cv2.putText(frame, 'press on q to close', (30, 460), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 255), 2)

            # show new Frame
            cv2.imshow('frame', frame)

            # break when q key pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # stop video when recognize someone known.
            if find_face: 
                if (self.face_locations != []) and (any(name != "Unknown" for name in self.face_names)):
                    stop_video_flag = True

        # stop video stream
        videostream.release()
        # cv2.destroyAllWindows()

        return stop_video_flag

        


if __name__ == '__main__':
    v=Video_Class()
    v.find_face_def()


