# 🚗 VEHICLE AND PEDESTRIAN DETECTION USING OPENCV

<p align="center">
  <img width="500" height="300" src="https://ckhconsulting.com/wp-content/uploads/2020/11/object-detection.gif">
</p>

---

## ❓ ABOUT THE PROJECT

This project is a real-time object detection system that identifies vehicles and pedestrians in video footage using OpenCV's Haar Cascade classifiers. It's a beginner-friendly project to understand how basic object tracking works using frame-by-frame video processing.

---

## 📄 FOLDER STRUCTURE
<pre lang="markdown"> ```bash vehicle-pedestrian-detection-opencv/ ├──   
  ├── main.py # Python script for detection  
  ├── requirements.txt # Required libraries  
  ├── Vehicles_and_Pedestrian_Tracking_Using_OpenCV.ipynb # Jupyter version  
  ├── haarcascades/ │   
    └──haarcascade_car.xml # Classifier for vehicle detection │  
    └── haarcascade_fullbody.xml # Classifier for pedestrian detection  
  ├── Dataset (Sample Videos)/  
    └── my_video.mp4 # Sample video input ``` </pre>

---

## 🛠️ HOW TO RUN

### 1. Clone the Repository and Install Requirements:
- git clone https://github.com/eshamnaik/vehicle-pedestrian-detection-opencv.git 
- cd vehicle-pedestrian-detection-opencv  
- pip install -r requirements.txt  
- python main.py  
---  
 🔍 WHAT TO EXPECT FROM THE OUTPUT  

✅ This is what happens after running the script:**  

🟢 **Code finishes successfully after:** `python main.py`    
📽️ The video will display frame-by-frame, with object detection.)  
🔴 **Red Boxes** → Detected **Vehicles**   
🟡 **Yellow Boxes** → Detected **Pedestrians**  

##CREDITS
https://towardsdatascience.com/how-to-detect-objects-in-real-time-using-opencv-and-python-c1ba0c2c69c0
https://pypi.org/project/opencv-python/

CREATOR- https://github.com/theshredbox
