from ultralytics import YOLO
import cv2
image = "000191.png";
model_tpy = "yolo11n-seg.pt"




def show_labels(results):
    for r in results:
        print("-" * 50)
        if len(r.boxes) == 0:
            print("  (no objects detected)")
            continue
        for i in range(len(r.boxes)):
            cls_id = int(r.boxes.cls[i])
            name   = model.names[cls_id]
            conf   = float(r.boxes.conf[i])
            box    = r.boxes.xyxy[i].tolist()

            print(f"  [{i}] {name:<15} conf={conf:.2f}  "f"box=({box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f})")
        print("-" * 50)
        
            
model = YOLO(model_tpy)  

results = model(image)
results[0].show()

show_labels(results)