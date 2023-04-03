###Experimenting with other approacches
# import streamlit as st
# from datetime import date
# #import phropet from fbprophet
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
# from plotly import graph_objs as go

# START = "2015-01-01"
# TODAY = date.today().strftime("%Y-%m-%d")

# st.title("Stock Predicition on the GSE")

# stocks = ("AADS","ABL")
# selected_stocks = st.selectbox("select dataset for prediction", stocks)

# n_years = st.slider("Years of prediction:", 1,2, 3)
# period = n_years*365

# Import packages and data
# import streamlit as st

from helper import*
import os

#Render page with Streamlit
st.title("Stock Predicition on the GSE")

stocks = ("AADS","ACCESS","AGA","ETI","MTNGH","SCB","TLW","TOTAL")
selected_stocks = st.selectbox("select dataset for prediction", stocks)

n_years = st.slider("Years of prediction:", 1,2, 3)
period = n_years*365

#Load data

data_load_state = st.text("Loading data...")

df = load_data(selected_stocks)
data_load_state.text("Loading data...done!")

#plot_opening(df)
st.subheader('Raw Data')
st.write(df.tail())
plot_opening(df)

#plot forecast
st.subheader('Forecast')

#get forecast
forecast, future = train_prophet(df,period)
