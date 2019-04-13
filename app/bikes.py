import os
import pandas as pd
import numpy as np

WEEKDAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def load_data():
    data_path = os.path.join('data', 'hour.csv')
    return pd.read_csv(data_path)


def stdev():
    df = load_data()

    daily = df.groupby(['dteday']).agg({'weekday': 'mean', 'casual': 'sum', 'registered': 'sum'})

    weekdays = daily.groupby(['weekday']).std()

    casual = dict(zip(WEEKDAY_NAMES, weekdays['casual'].tolist()))
    registered = dict(zip(WEEKDAY_NAMES, weekdays['registered'].tolist()))

    return {'stdev': {'casual': casual, 'registered': registered}}
