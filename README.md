<h1 align="center">💊 Pill Detection System</h1>
<p align="center"><i>Detect pills in images using a fine-tuned YOLO model</i></p>

---

# 🌟 Overview

This project is a **computer vision-based pill detection system** that identifies pills in images using object detection.

The model is trained using a **Kaggle pill image dataset** and fine-tuned with **YOLOv11m** to accurately detect pill locations in real-world images.

---

# 🎯 Objective

- Detect pills from input images
- Localize pills using bounding boxes
- Build a strong foundation for future pill identification systems

---

# 🧠 Model

- Model: **YOLOv11m**
- Task: **Object Detection**
- Training: **Fine-tuning on custom dataset**
- Dataset Source: **Kaggle pill dataset**

---

# 📊 Dataset

- Images of pills with labeled bounding boxes
- Includes variations in:
  - Lighting conditions
  - Backgrounds
  - Pill shapes and sizes

---

# ⚙️ Training Details

- Image size: 640
- Batch size: 48
- Epochs: 100
- Early stopping (patience): 15
- Device: GPU (multi-GPU supported)

---

# 🔍 Detection Pipeline
