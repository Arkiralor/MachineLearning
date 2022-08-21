# Machine Learning

The repository I use to learn application of ML concepts.

## Setup

1. `python -m venv env`
2. `source env/Scripts/activate`
3. `python -m pip install --upgrade pip==22.0.4`
4. `python -m pip install pip-tools`
5. `pip-compile`
6. `python -m pip install -r requirements.txt`

## Dataset

1. Video Game Sales by [Gregory Smith on Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales)

## Functionality

1. Based on the attributes: [`Platform`, `Genre`, `Release Year`, `Publisher`], the model predicts the global sales performance of a Video Game.
2. The Sales Performance categories are as follows:
    - _Less than 60'000 copies sold globally:_ __Extremely Poor__
    - _Between 60'000 and 250'000 copies sold globally:_ __Poor__
    - _Between 250'000 and 500'000 copies sold globally:_ __Average__
    - _Between 500'000 and 1'000'000 copies sold globally:_ __Acceptable__
    - _Between 1'000'000 and 5'000'000 copies sold globally:_ __Good__
    - _Between 5'000'000 and 10'000'000 copies sold globally:_ __Very Good__
    - _Between 10'000'000 and 15'000'000 copies sold globally:_ __Excellent__
    - _Greater than 15'000'000 copies sold globally:_ __Bestseller__
3. The split between `training` vs `test` data is `9:1`.
