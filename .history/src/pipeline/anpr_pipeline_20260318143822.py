import cv2
from src.detection.plate_detector import PlateDetector
from src.ocr.ocr_reader import OCRReader
from src.utils.image_processing import preprocess
from src.utils.text_cleaner import clean_text

class ANPRPipeline:
    def __init__(self, model_path):
        self.detector = PlateDetector(model_path)
        self.ocr = OCRReader()

    def run(self, image_path):
        image = cv2.imread(image_path)

        boxes = self.detector.detect(image)

        results = []

        for (x1, y1, x2, y2) in boxes:
            plate = image[y1:y2, x1:x2]

            plate = preprocess(plate)

            texts = self.ocr.read(plate)

            for text in texts:
                results.append(clean_text(text))

        return results