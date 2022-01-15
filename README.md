# Human_identification_capabilities

This repo build to learn computer vision and image processing.   
I use [face_recognition](https://github.com/ageitgey/face_recognition) and opencv2 for this task.   
This repo build on raspberry pi 4 + pi camera -FYI the FPS is very slow.


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
note : raspistill has been replaced by libcamera,this repo still use raspistill.

4) make sure you install this dependencies:

```
sudo apt-get install libatlas-base-dev
```

5) run 
```
python3 GUI.py
```

