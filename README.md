# Human_identification_capabilities

This repo build to demonstrate human identification capabilities - 
1) Detect new faces -  see a new person , remember his facial features in memory and classify it by name. 
2) Identification  - see familiar person and say his name.

My goal is to learn computer vision, image processing, GUI .    
I use [face_recognition](https://github.com/ageitgey/face_recognition) , opencv2 and Tkinter for this task.


notes :
1) The face_recognition library use "dlib" library. 
2) Behind the scenes - to detect face "dlib" use HOG(Histogram of Oriented Gradients) model.  
I recommend reading this article to understand how the HOG works -
https://medium.com/analytics-vidhya/a-take-on-h-o-g-feature-descriptor-e839ebba1e52

3) This repo build on raspberry pi 4 + pi camera -FYI the FPS is very slow.
4) this repo still use raspistill ,raspistill has been replaced by libcamera.


# Get startted  
1) build venv 
```
python3 -m venv venv
```
2) Install requirements at virtual environments
```
source venv/bin/activate
pip install -r requirements.txt
```

3) make sure camera connected , you can follow this tutorial : <br>
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2 <br>


4) make sure you install this dependencies:

```
sudo apt-get install libatlas-base-dev
```

5) run GUI -
```
python GUI.py
```

6) GUI have 2 option :  
a. "Who is it?" - detect face in front of the camera and if we see familiar face ,the PI will say his name.  
b. "Add new face"  - will look for unknown faces and classify them with the name you enter in the input field.  
![image](https://user-images.githubusercontent.com/82320340/153349685-66a8e63c-8655-473a-bf75-c611a2528931.png)


