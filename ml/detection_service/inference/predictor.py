from ml.detection_service.inference.model_load import load_model

def detect_single_pill(path_name: str):
    """
    Runs YOLO object detection on a single image and returns pill detections.

    Args:
        path_name (str): Path to the input image file.

    Returns:
        list[dict]: A list of detections where each detection contains:
            - bounding_box: (x1, y1, x2, y2) pixel coordinates
            - confidence: model confidence score
            - class_id: predicted class index

    Notes:
        Coordinates use the `xyxy` box format:
            (x1, y1) = top-left corner
            (x2, y2) = bottom-right corner
        .tolist() and .item() are used to convert tensors to standard Python types(tensor -> list, pytorch tensor -> real python float/int).
    """
    model = load_model()
    result = model(path_name, conf = 0.5) # Set confidence threshold to 50%

    detections = []

    for r in result:
        if r.boxes is not None:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())
                
                detections.append({
                    "bounding_box": {
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2
                    },
                    "confidence": conf,
                    "class_id": cls
                })

    return detections