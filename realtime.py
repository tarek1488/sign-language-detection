from ultralytics import YOLO

# Use raw string literals to avoid invalid escape sequences
model = YOLO(r"runs\detect\train3\weights\best.pt")

results = model.predict(source="0", show=True)



print(results)
