import pandas as pd

from os import path

from .config.settings import BASE_DIR

## Path to dataset
dataset = path.join(BASE_DIR, "data", "vgsales_cleaned.csv")

## Read data
DATA_FRAME = pd.read_csv(dataset)

## preliminary cleaning
DATA_FRAME = DATA_FRAME.drop(columns=['Unnamed: 0', 'Rank', 'Name'], axis=1)
DATA_FRAME = DATA_FRAME.dropna()

GENRE = {i: j for i, j in enumerate(DATA_FRAME['Genre'].unique().tolist())}
PLATFORM = {i: j for i, j in enumerate(DATA_FRAME['Platform'].unique().tolist())}
PUBLISHER = {i: j for i, j in enumerate(DATA_FRAME['Publisher'].unique().tolist())}

if __name__=="__main__":
    print(DATA_FRAME.head(16))