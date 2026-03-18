import easyocr

class OCRReader:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def read(self, image):
        results = self.reader.readtext(image)
        texts = [res[1] for res in results]
        return texts