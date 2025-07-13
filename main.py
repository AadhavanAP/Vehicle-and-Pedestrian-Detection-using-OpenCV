import cv2
import os

# Get the directory where the current script is located
script_dir = os.path.dirname(__file__)

# Absolute path to the video file (adjust as needed)
video_path = '/Users/aadhavanap/Downloads/vehicle-pedestrian-detection-opencv-master/Dataset (Sample Videos)/WhatsApp Video 2025-07-08 at 14.03.20.mp4'

# Construct classifier paths relative to the script directory
car_path = os.path.join(script_dir, 'haarcascades', 'haarcascade_car.xml')
pedestrian_path = os.path.join(script_dir, 'haarcascades', 'haarcascade_fullbody.xml')

# Debug prints
print("Video path exists:", os.path.exists(video_path))
print("Car path exists:", os.path.exists(car_path))
print("Pedestrian path exists:", os.path.exists(pedestrian_path))

# Load classifiers
car_tracker = cv2.CascadeClassifier(car_path)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_path)

# Validate classifier loading
if car_tracker.empty():
    print(f"Error: Could not load car cascade classifier from {car_path}")
    exit()
if pedestrian_tracker.empty():
    print(f"Error: Could not load pedestrian cascade classifier from {pedestrian_path}")
    exit()

# Open video file
video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print(f"Error: Could not open video from {video_path}")
    exit()

while True:
    (read_successful, frame) = video.read()

    if not read_successful:
        print("End of video stream or error reading frame.")
        break

    # Convert frame to grayscale
    greyscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    greyscaled_frame = clahe.apply(greyscaled_frame)

    # Apply Gaussian blur to reduce noise
    greyscaled_frame = cv2.GaussianBlur(greyscaled_frame, (3, 3), 0)

    # Detect vehicles
    cars = car_tracker.detectMultiScale(
        greyscaled_frame,
        scaleFactor=1.05,
        minNeighbors=8,
        minSize=(30, 30),
        maxSize=(300, 300),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Detect pedestrians
    pedestrians = pedestrian_tracker.detectMultiScale(
        greyscaled_frame,
        scaleFactor=1.03,
        minNeighbors=6,
        minSize=(20, 60),
        maxSize=(100, 300),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around vehicles
    for (x, y, w, h) in cars:
        if w > 25 and h > 25 and w < 350 and h < 350:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(frame, 'VEHICLE', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, f'W:{w} H:{h}', (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

    # Draw rectangles around pedestrians
    for (x, y, w, h) in pedestrians:
        if w > 15 and h > 50 and h > w * 1.5 and w < 120 and h < 350:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
            cv2.putText(frame, 'HUMAN', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(frame, f'W:{w} H:{h}', (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)

    # Show frame
    cv2.imshow('Vehicle and Pedestrian Detector', frame)

    # Exit on 'q' key
    key = cv2.waitKey(1)
    if key == ord('q') or key == ord('Q'):
        break

# Clean up
video.release()
cv2.destroyAllWindows()
