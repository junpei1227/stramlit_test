import streamlit as st 
import pandas as pd 
import numpy as np


st.title("hello")
df = pd.read_csv("book_list.csv")

st.dataframe(df)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [35.66, 139.4],
    columns=['lat', 'lon'])

st.map()