from ultralytics import YOLO

class PlateDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, image):
        results = self.model(image)
        boxes = []

        for r in results:
            for box in r.boxes.xyxy:
                boxes.append(list(map(int, box)))

        return boxes