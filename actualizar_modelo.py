import pandas as pd


from fraudes.python.src.prepare import data_preparada, save_data_preparada
from fraudes.python.src.train import train_model


if __name__ == '__main__':
    data_preparada()
    save_data_preparada()
    train_model()
