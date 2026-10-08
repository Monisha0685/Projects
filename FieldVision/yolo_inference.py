from ultralytics import YOLO

model = YOLO("models/best.pt")

results = model.predict("input_videos/08fd33_4.mp4", save=True)
print(results[0])

print("======================================================================")

#method .boxes to show all the object of a bounding box
for box in results[0].boxes:
    print(box)