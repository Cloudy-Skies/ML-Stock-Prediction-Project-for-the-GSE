import streamlit as st
from datetime import date

from fbprophet import prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Predicition on the GSE")

stocks = ("AADS","ABL")
selected_stocks = st.selectbox("select dataset for prediction", stocks)

n_years = st.slider("Years of prediction:", 1,2, 3)
period = n_years*365
