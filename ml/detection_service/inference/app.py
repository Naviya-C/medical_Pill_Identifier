from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

import streamlit as st

model = YOLO(
    "/home/naviya-c/Desktop/Projects/pill-id-platform/ml/detection_service/inference/models/best_YOLOv11m-v1.pt"
)

st.title("💊 Pill Detection System")

upload_file = st.file_uploader("Upload Image", type=["jpg","png", "jpeg"])

if upload_file:
    image = Image.open(upload_file)
    img_array = np.array(image)
    
    result = model.predict(
        img_array,
        imgsz = 640,
        conf = 0.25
        ) 
    
    annotate = result[0].plot()
    
    st.image(annotate, caption = "Pills")