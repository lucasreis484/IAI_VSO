from ultralytics import YOLO
import cv2
import csv
import cvzone
import math
import time
import os
import glob
from pathlib import Path
import numpy as np
import statistics

source = r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\12\image_0"
model_seg = "yolo11l-seg.pt"
model_deph = "yolo26n-depth.pt"
V_imgsz = 640

output = "output"
segmentation = YOLO(model_seg)  
depth = YOLO(model_deph)
def get_mask():
    #adasdasdasda
    print("Hello World")
    print("Hello World")
class Objects:
    """Registers objects by (id, class), counting how many and storing the distances."""

    # {"(id, class)": {"quantity": int, "distances": [float, ...]}}
    _registry = {}

    def __init__(self, id, obj_class, distance):
        self.id = id
        self.obj_class = obj_class
        self.distance = distance

        key = (id, obj_class)   # tuple = composite key

        if key in Objects._registry:
            # Same id AND same class → increment and append the distance
            Objects._registry[key]["quantity"] += 1
            Objects._registry[key]["distances"].append(distance)
        else:
            # New combination → create with 1 and the list with the first distance
            Objects._registry[key] = {
                "quantity": 1,
                "distances": [distance]
            }

    @classmethod
    def quantity(cls, id, obj_class):
        """Returns how many objects with this (id, class) exist."""
        return cls._registry.get((id, obj_class), {}).get("quantity", 0)

    @classmethod
    def distances(cls, id, obj_class):
        """Returns the list of distances for this (id, class)."""
        return cls._registry.get((id, obj_class), {}).get("distances", [])

    def __repr__(self):
        return f"Objects(id={self.id}, class={self.obj_class}, distance={self.distance})"
    @classmethod
    def to_csv(cls, filename="registry.csv"):
        """Exports the full registry to a CSV file."""
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "class", "quantity", "distances"])

            for (id, obj_class), data in cls._registry.items():
                # Join distances into a single string, e.g. "10.5;15.3;5.0"
                dist_str = ";".join(str(d) for d in data["distances"])
                writer.writerow([id, obj_class, data["quantity"], dist_str])

        print(f"CSV exported to '{filename}'")



os.makedirs(output, exist_ok=True)

image_files = glob.glob(os.path.join(source, "*.png"))

image_files.sort()

print(f"Found {len(image_files)} PNG images to process")

for idx, image_path in enumerate(image_files):
    print(f"Processing image {idx + 1}/{len(image_files)}: {os.path.basename(image_path)}")
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error reading image: {image_path}")
        continue
    results = segmentation.track(img, persist=True,  tracker=r"venv\Lib\site-packages\ultralytics\cfg\trackers\bytetrack_copy.yaml",stream=True, verbose = False)
    for r in results:
        boxes = r.boxes
        
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            conf = math.ceil((box.conf[0] * 100)) / 100   
            track_id = int(box.id[0]) if box.id is not None else None
            cls_id = int(box.cls[0])
            if( segmentation.names[cls_id] == "car" or segmentation.names[cls_id] == "truck"or segmentation.names[cls_id] == "motorclycle") and (track_id is not None):
                Objects(track_id,segmentation.names[cls_id],100) 
            print("\ntrack_id: ", track_id, "\n classe: ", segmentation.names[cls_id], "\nQuantidade: ", Objects.quantity(track_id,segmentation.names[cls_id]), "\nQuantidade: ", Objects.distances(track_id,segmentation.names[cls_id]))
            if track_id is not None:
                label = f'ID {track_id} {segmentation.names[cls_id]} {conf}'
            else:
                label = f'{segmentation.names[cls_id]} {conf}'

            cvzone.putTextRect(
                img, label,
                (max(0, x1), max(35, y1)),
                scale=1, thickness=1
            )
    output_path = os.path.join(output, os.path.basename(image_path))
    cv2.imwrite(output_path, img)
    print(f"Saved: {output_path}")
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Processing interrupted by user")
        break

cv2.destroyAllWindows()

print("Processing complete.")
Objects.to_csv()
