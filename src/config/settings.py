from os import path

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

if __name__ == "__main__":
    print(BASE_DIR)