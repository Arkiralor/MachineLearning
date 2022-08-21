from src.data_frame import DATA_FRAME
from src.model import Model
from src.config.settings import BASE_DIR

from os import path

def setup():
    print("No model found; creating & training from dataset.")
    df = DATA_FRAME
    print(f"Created the dataFrame: \n{df}")
    model = Model(df)
    print(f"Created the model: \n{model.__module__}")
    model.make_sets()
    print(f"Created the independent datasets for training and testing.")
    _, _, x_test, y_test = model.x_train, model.y_train, model.x_test, model.y_test

    print("Training the model.")
    model.train_model()

    return model, x_test, y_test

def main():
    print("Seting Up...")
    model, x_test, y_test = setup()
    
    test_predictions = list(model.predict(x_test))
    print(f"Test Data Predictions truncated to first 10 items (Prediction, Actual): {list(zip(test_predictions, list(y_test)))[0:10]}")

    print("Scoring the model's predictions.")
    model_score = model.score(x_test, y_test)
    print(f"Model score: {model_score}")

    if model_score > 0.9:
        model_path = path.join(BASE_DIR, "models", "vgsale_model.joblib")
        model.export_model(model_path)
        print(f"Model exported to {model_path}")


if __name__ == "__main__":
    main()
