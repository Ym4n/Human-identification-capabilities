# Human_identification_capabilities

This repo is built to demonstrate human identification capabilities such as- - 
1) Detect new faces - see a new person, remember his facial features in memory and classify it by name. 
2) Identification - see familiar person and say his name.

My goal is to learn computer vision, image processing, GUI .    
For this task I use [face_recognition](https://github.com/ageitgey/face_recognition) , [opencv2](https://pypi.org/project/opencv-python/) , [Tkinter](https://docs.python.org/3/library/tkinter.html) and [gTTS](https://gtts.readthedocs.io/en/latest/) .

Notes :
1) The face_recognition library use "dlib" library. 
2) Under the hood - The library “dilb”, uses HOG(Histogram of Oriented Gradients) model in order to detect the face.
In order to understand how HOG works, I recommend reading this article -
https://medium.com/analytics-vidhya/a-take-on-h-o-g-feature-descriptor-e839ebba1e52

3) This repo was built on raspberry pi 4 + pi camera -FYI the FPS is very slow.
4) This repo still uses raspistill ,raspistill has been replaced by libcamera.
5) I used gTTS library to create For Text-to-Speech - FYI need internet connection .


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
![image](https://user-images.githubusercontent.com/82320340/153349685-66a8e63c-8655-473a-bf75-c611a2528931.png)

a. "Who is it?" - detect a face in front of the camera and if it’s a familiar face ,the PI will say the person’s name.  
b. "Add new face" - will look for unknown faces and classify them with the name you enter in the input field.  


here exmple with obama-  
![image](https://user-images.githubusercontent.com/82320340/153770024-12d7c8d3-5285-4ffc-9f60-7db82a858c2c.png)


Enjoy :)
