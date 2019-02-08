
import time

import pandas as pd


def load_data(filename):
    with open(filename, encoding='UTF-8') as f:
        data = pd.read_csv(f, sep=',', lineterminator='\n')  # TODO check dtype?
        return data


def get_dummies(df_input, columns):
    for column in columns:
        if df_input[column].isnull().sum() == 0:
            df_input = pd.get_dummies(df_input, columns=[column], dummy_na=False)
        else:
            df_input = pd.get_dummies(df_input, columns=[column], dummy_na=True)  # one extra category there are nulls
        df_input = df_input.iloc[:, :-1]  # removes linear dependencies
    return df_input
