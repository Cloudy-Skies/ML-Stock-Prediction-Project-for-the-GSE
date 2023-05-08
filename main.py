###Experimenting with other approacches
# import streamlit as st
# from datetime import date
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
# from plotly import graph_objs as go

# START = "2015-01-01"
# TODAY = date.today().strftime("%Y-%m-%d")

# st.title("Stock Predicition on the GSE")

# stocks = ("AADS","ABL")
# selected_stocks = st.selectbox("select dataset for prediction", stocks)

# n_weeks = st.slider("Years of prediction:", 1,2, 3)
# period = n_years*365

# Import packages and data
# import streamlit as st

from helper import*
import os

#Render page with Streamlit
st.title("Stock Predicition on the GSE")

stocks = ("AADS","ACCESS","AGA","ETI","MTNGH","SCB","TLW","TOTAL")
selected_stocks = st.selectbox("select dataset for prediction", stocks)

n_months = st.slider("Weeks of prediction:", 1,3,5)
period = n_months*30

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
forecast, future,m = train_prophet(df,period)

st.subheader('Forecast Data')
st.write(forecast.tail())
fig1 = plot_plotly(m,forecast)
st.plotly_chart(fig1)

st.write('Forecast Components')
fig2=m.plot_components(forecast)
st.write(fig2)

