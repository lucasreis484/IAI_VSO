from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import os
import glob

# Load YOLO model
model = YOLO("../Yolo-Weights/yolov8l.pt")

# Input folder with images
input_folder =  r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\00\image_0"  # Pasta com as imagens de entrada
output_folder = "output_frames"  # Pasta para salvar as imagens processadas

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

# Get list of all image files in input folder
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff']
image_files = []
for ext in image_extensions:
    image_files.extend(glob.glob(os.path.join(input_folder, ext)))
    image_files.extend(glob.glob(os.path.join(input_folder, ext.upper())))

# Sort image files by name
image_files.sort()

print(f"Found {len(image_files)} images to process")

# Process each image
for idx, image_path in enumerate(image_files):
    print(f"Processing image {idx + 1}/{len(image_files)}: {os.path.basename(image_path)}")
    
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error reading image: {image_path}")
        continue
    
    # Perform object detection with YOLO
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
    
    # Save processed image with same filename in output folder
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_path, img)
    print(f"Saved: {output_path}")
    
    # Optional: Display image (press 'q' to skip, any other key to continue)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Processing interrupted by user")
        break

cv2.destroyAllWindows()

# Optional: Create video from processed images (if you want)
create_video = False  # Set to True if you want to create a video from the processed images

if create_video and len(image_files) > 0:
    output_video_path = "output_video.mp4"
    img_array = []
    
    # Read all processed images
    processed_files = sorted(glob.glob(os.path.join(output_folder, "*.jpg")) + 
                             glob.glob(os.path.join(output_folder, "*.png")))
    
    for filename in processed_files:
        img = cv2.imread(filename)
        if img is not None:
            height, width, layers = img.shape
            size = (width, height)
            img_array.append(img)
    
    if img_array:
        out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
        for img in img_array:
            out.write(img)
        out.release()
        print("Video created successfully.")
    else:
        print("No images found to create video.")

print("Processing complete.")