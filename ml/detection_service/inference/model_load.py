from ultralytics import YOLO

def load_model():
    return YOLO("yolov10x.pt") #Lightweight model for local cpu testing