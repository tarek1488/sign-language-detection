from ultralytics import YOLO

model = YOLO("yolov8n.pt") # loading the pretrained model 

model.train(data = 'config.yaml', epochs=20)
