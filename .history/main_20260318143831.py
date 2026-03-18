from src.pipeline.anpr_pipeline import ANPRPipeline

if __name__ == "__main__":
    pipeline = ANPRPipeline("models/best.pt")

    results = pipeline.run("data/raw/car.jpg")

    print("Detected Plates:", results)