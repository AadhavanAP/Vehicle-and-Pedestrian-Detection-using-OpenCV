import cv2
import os

# Get the directory where the current script (main.py) is located
script_dir = os.path.dirname(__file__)

# Construct paths relative to the script's directory
video_path = os.path.join(script_dir, 'Dataset (Sample Videos)', 'my_video.mp4')
car_path = os.path.join(script_dir, 'haarcascades', 'haarcascade_car.xml')
pedestrian_path = os.path.join(script_dir, 'haarcascades', 'haarcascade_fullbody.xml')

# Debug prints to make sure paths are correct
print("Video path exists:", os.path.exists(video_path))
print("Car path exists:", os.path.exists(car_path))
print("Pedestrian path exists:", os.path.exists(pedestrian_path))

# Load classifiers
car_tracker = cv2.CascadeClassifier(car_path)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_path)

# Check if classifiers loaded successfully
if car_tracker.empty():
    print(f"Error: Could not load car cascade classifier from {car_path}")
    exit()
if pedestrian_tracker.empty():
    print(f"Error: Could not load pedestrian cascade classifier from {pedestrian_path}")
    exit()

video = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not video.isOpened():
    print(f"Error: Could not open video from {video_path}")
    exit()

while True:
    (read_successful, frame) = video.read()

    if not read_successful:
        print("End of video stream or error reading frame.")
        break

    greyscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Adjust scaleFactor and minNeighbors for better detection if needed
    cars = car_tracker.detectMultiScale(greyscaled_frame, scaleFactor=1.1, minNeighbors=5)
    pedestrians = pedestrian_tracker.detectMultiScale(greyscaled_frame, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, 'VEHICLE', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 70), 2)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(frame, 'HUMAN', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    cv2.imshow('Vehicle and Pedestrian Detector', frame)

    key = cv2.waitKey(1)
    if key == ord('q') or key == ord('Q'):
        break

video.release()
cv2.destroyAllWindows()