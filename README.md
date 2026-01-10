<h1 align="center">💊 Pill-ID Platform</h1>
<p align="center"><i>"Point your camera at a pill. We'll tell you what it is."</i></p>

---

# 🌟 Overview

Pill-ID Platform is an AI-driven system for identifying medication pills from images by combining:

✔ Object Detection  
✔ Segmentation  
✔ OCR (future)  
✔ Visual Classification  
✔ Feature Fusion  
✔ Vector Similarity (future)  
✔ Metadata Database Matching  
✔ Ranking + Confidence Scoring  

Designed for:

- Pharmacies
- Hospitals
- Telemedicine platforms
- Caregivers
- Consumers

---

# 🎬 End-to-End Processing Pipeline

```
📸 Input Image
        ↓
🧽 Preprocessing (resize, normalize, enhance)
        ↓
🔍 Object Detection (YOLOv9/YOLOv10)
        ↓
✂️ Segmentation (SAM / Mask-RCNN)
        ↓
🧠 Feature Extraction
     ├─ Color + Shape
     ├─ Visual Embedding (ViT / EfficientNet)
     ├─ Imprint Text (OCR - future)
        ↓
🧩 Feature Fusion (Hybrid Rule + ML)
        ↓
🗄 Database Matching + Ranking
        ↓
🎯 Final Pill Identification + Confidence
```

---

# 🧱 Architecture Overview

The platform is built as a **microservice architecture** so components can scale independently.

### 🟦 High-Level Architecture Diagram (Text Form)

```
User → Web UI (React)
          ↓
     API Gateway (Go)
          ↓
 ┌───────────────────────────────┐
 │   ML Inference Services       │
 │   (Python, GPU + CPU)         │
 │  ├─ Detection Service         │
 │  ├─ Segmentation Service      │
 │  ├─ Classification Service    │
 │  ├─ Embedding Service         │
 │  └─ Fusion Service            │
 └───────────────────────────────┘
          ↓
 ┌───────────────────────────────┐
 │      Data Services (Go)       │
 │  ├─ Pill Metadata → Postgres  │
 │  └─ Vector Search → OpenSearch│
 └───────────────────────────────┘
          ↓
        S3 Storage
```

⭐ **Visual PNG/SVG diagrams** are located in:

```
docs/architecture/
```

---

# 🤖 Model Selection & Justification

Pill recognition is multi-modal. We assign different models to different tasks:

| Task | Model | Reason |
|---|---|---|
| Detection | **YOLOv9 / YOLOv10** | Fast, accurate, real-time on GPU |
| Segmentation | **SAM / MaskRCNN** | Clean pill boundary extraction |
| Classification | **ViT / EfficientNet** | Strong accuracy on small objects |
| Embeddings | **CLIP / ArcFace** | Useful for retrieval + similarity |
| OCR (future) | **TrOCR / PaddleOCR** | Extract imprint characters |
| Fusion | Hybrid Rule + ML | Combines multiple modalities |
| Retrieval (future) | **FAISS / OpenSearch** | Vector search on embeddings |

---

# 🧠 Why YOLOv9/YOLOv10?

Compared to FasterRCNN / DETR / SSD, YOLOv9/10 offers:

✔ Higher FPS  
✔ Better mAP on small objects  
✔ GPU-friendly  
✔ Low latency for real-time apps  
✔ Excellent for **phone images** (primary input source)

Detection matters because pills often:

- are small objects
- appear on various backgrounds
- differ subtly

---

# 🧰 Hardware-Aware Model Deployment

Inference assignment:

| Service | Compute |
|---|---|
| Detection | **GPU (EC2)** |
| Segmentation | **GPU (EC2)** |
| Classification | **GPU (EC2)** |
| Embeddings | CPU or GPU |
| Fusion | CPU |
| DB Services | CPU |
| Frontend | Browser/client |
| API Gateway | CPU |

---

# 🗄 Database & Storage Architecture

The platform uses 3 storage layers:

### 🟦 1. Object Storage → **Amazon S3**

Stores:

- user images
- segmented crops
- training data
- model weights
- inference logs

---

### 🟨 2. Structured DB → **PostgreSQL (AWS RDS)**

Stores pill metadata:

| Field | Example |
|---|---|
| name | Acetaminophen |
| strength | 500mg |
| color | White |
| shape | Capsule |
| manufacturer | Aurobindo Pharma |
| ndc | 12345-6789 |
| imprint | "IP 204" |
| image refs | s3://... |

---

### 🟩 3. Vector Search (Future) → **AWS OpenSearch / FAISS**

For similarity search using embeddings:

```
Query Embedding → k-NN → Top Candidates
```

---

# 🧪 Training Plan

Training is executed in **5 phases**:

### **Phase 1: Detection Training**
- Dataset: bounding-box annotated pills
- Model: YOLOv9/10
- Metrics: `mAP@[0.5:0.95]`

### **Phase 2: Segmentation Training**
- Dataset: masks (SAM-assisted)
- Metrics: `IoU / Dice`

### **Phase 3: Classification Training**
- Dataset: 200 pill classes
- Augmentations: lighting, zoom, blur, rotation, background
- Metrics: `Top-1 / Top-3 Accuracy`

### **Phase 4: Embeddings (future)**
- Model: CLIP / ArcFace + Triplet Loss
- Metrics: `Recall@K (K=1,3,5)`

### **Phase 5: Fusion & Validation**
- Evaluate entire pipeline end-to-end
- Metric: Pill Identification Accuracy

---

# ☁️ AWS Deployment Architecture

Components:

```
CloudFront → API Gateway → ECS Cluster
                          ├─ GPU EC2 Nodes (ML)
                          └─ Fargate CPU Nodes (Services)
```

AWS Services Used:

| Component | AWS Service |
|---|---|
| Compute (GPU) | EC2 G5 / G6 |
| Compute (CPU) | ECS Fargate |
| Object Storage | S3 |
| Structured DB | RDS PostgreSQL |
| Vector DB | OpenSearch |
| Authentication | Cognito |
| CDN | CloudFront |
| API Proxy | API Gateway |
| Monitoring | CloudWatch |
| Metrics | X-Ray |
| Messaging | SQS / SNS |
| Container Registry | ECR |

---

# 🧩 Microservices Architecture

Microservices built in **Go (business)** + **Python (ML)**:

---

### 🟦 Python ML Services

```
ml/
 ├── detection-service/
 ├── segmentation-service/
 ├── classification-service/
 ├── embedding-service/
 └── fusion-service/
```

---

### 🟨 Go Data & Control Services

```
backend/
 ├── api-gateway/
 ├── auth-service/
 ├── pill-db-service/
 ├── vector-search-service/
 ├── logging-service/
 └── notification-service/
```

---

# 🏗 Repository Structure (Simplified)

```
pill-id-platform/
 ├── frontend/
 ├── backend/
 ├── ml/
 ├── database/
 ├── deployments/
 ├── docs/
 └── ci-cd/
```

---

# 🔁 Versioning Strategy (SemVer)

```
MAJOR.MINOR.PATCH
```

Planned:

```
v0.1.0 → MVP (single pill classification)
v0.2.0 → Multi-pill + OCR
v1.0.0 → Full pipeline w/ vector search
v2.0.0 → Enterprise: offline + HIPAA + telemed
```

---

# 🗺 Roadmap

### **v0.1.x — MVP**
✔ Single pill  
✔ Classification  
✔ Metadata lookup  

### **v0.2.x — Multi-Pill**
✔ Detection  
✔ Segmentation  
✔ OCR  

### **v1.0.0 — Production**
✔ Embeddings  
✔ Fusion  
✔ Vector Search  
✔ AWS Deployment  
✔ Auth + Observability  

### **v2.x — Enterprise**
✔ Offline inference  
✔ Regulatory alignment  
✔ Telemedicine API  
✔ Pharmacist workflows  

---

# 🤝 Contributions

Looking for collaborators with backgrounds in:

- ML/CV
- Backend Systems
- Healthcare Software
- Pharmaceutical Data

---

# 📜 License

TBD (commercial strategy dependent)

---

# 🚀 Status

`Current Phase: MVP → Full Pipeline`
