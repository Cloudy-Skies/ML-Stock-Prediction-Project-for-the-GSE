import pandas as pd
from plotly import graph_objs as go
import streamlit as st
from prophet import Prophet
import requests
import io


@st.cache_data
def load_data(code):
    # download data from github repo
    url = "https://raw.githubusercontent.com/Cloudy-Skies/ML-Stock-Prediction-Project-for-the-GSE/master/Data/"+code+".csv"
    download = requests.get(url).content

    #read data
    df = pd.read_csv(io.StringIO(download.decode('utf-8')))

    #convert string to date
    df["Daily Date"]=pd.to_datetime(df["Daily Date"],dayfirst=True)
    df["Daily Date"] = df["Daily Date"].reset_index(drop=True)

    #sorting the dates from highest to lowest
    df.sort_values(by="Daily Date")
    return df

#Plot Opening Price
def plot_opening(df):
    plot_data(df, "Opening Price (GH¢)", "Daily Date", "Opening Price (GH¢)")

def plot_change(df):
    plot_data(df, "Price Change (GH¢)", "Daily Date", "Price Change (GH¢)")

#Generic Plot function
def plot_data(df, title, xlabel, ylabel):
    # Creating the figure
    fig = go.Figure()

    #Plotting the data
    fig.add_trace(go.Scatter(x=df[xlabel],y=df[ylabel],name=title))

    #Adding the xaxis slider
    fig.layout.update(title_text="Time Series Data",xaxis_rangeslider_visible=True) # type: ignore

    #Plotting the figure on Streamlit
    st.plotly_chart(fig)

# Training for prophet
def train_prophet(df,period):

    #
    df = df.reset_index()
    df = df.rename(columns={'Daily Date': 'ds', 'Opening Price (GH¢)': 'y'})
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)
    return forecast, future