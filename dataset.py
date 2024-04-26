import pandas as pd
import streamlit as st

DATA_URL = 'students_info.csv'

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.columns = [x.lower() for x in data.columns]  # More pythonic way to lower case column names
    data['date'] = pd.to_datetime(data['date'])  # Direct reference to the column
    return data

