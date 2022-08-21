from src.data_frame import DATA_FRAME
from src.model import Model
from src.config.settings import BASE_DIR

from os import path

def setup():
    print("No model found; creating & training from dataset.")
    df = DATA_FRAME
    print(f"Created the dataFrame: \n{df}")
    model = Model(df)
    print(f"Created the model: \n{model}")
    model.make_sets()
    print(f"Created the independent datasets for training and testing.")
    _, _, x_test, y_test = model.x_train, model.y_train, model.x_test, model.y_test

    print("Training the model.")
    model.train_model()

    return model, x_test, y_test

def main():
    print("Seting Up...")
    model, x_test, y_test = setup()
    

    print("Scoring the model's predictions.")
    model_score = model.score(x_test, y_test)
    print(f"Model score: {model_score}")

    if model_score > 0.9:
        model.export_model(path.join(BASE_DIR, "models", "vgsale_model.joblib"))
        print("Model exported")


if __name__ == "__main__":
    main()
