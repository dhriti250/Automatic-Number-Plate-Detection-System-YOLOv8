from src.pipeline.anpr_pipeline import ANPRPipeline

if __name__ == "__main__":
    pipeline = ANPRPipeline("yolov8n.pt")

    results = pipeline.run("data/raw/car.jpg")

    print("Detected Plates:", results)