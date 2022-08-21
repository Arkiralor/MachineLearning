from src.data_frame import DATA_FRAME
from src.model import Model

from os import path, getcwd

def main():
    df = DATA_FRAME
    model = Model(df)
    model.make_sets()
    _, _, x_test, y_test = model.x_train, model.y_train, model.x_test, model.y_test
    model.train_model()

    model_score = model.score(x_test, y_test)
    print(f"Model score: {model_score}")

    if model_score > 0.82:
        model.export_model(path.join(getcwd(), "models", "model.pkl"))
        print("Model exported")


if __name__ == "__main__":
    main()
