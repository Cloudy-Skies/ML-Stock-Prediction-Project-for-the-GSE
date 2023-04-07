import streamlit as st
from helper import*

st.title("Prophet Demo")
st.header("About Prophet")
desc = 'Prophet, otherwise known as Facebook Prophet or simply "fbprophet", is an open-source algorithm for forecasting time series data based on a model where non-linear trends are fit with yearly, weekly and daily seasonality as well as holiday effects'
with st.container():
    st.write(desc)
    with st.container():
        st.write("$y(t) = g(t) + s(t) + \epsilon_{(t)}$")
        st.write("$g(t)$ is the growth rate of the stock")
        st.write("$s(t)$ is the seasonal component of the stock")
        st.write("$\epsilon_{(t)}$ is the random component of the stock")
        #Button to open the link
        url = "https://facebook.github.io/prophet/"
        st.markdown("[Link to Prophet](%s)" % url, unsafe_allow_html=True)
        # st.write("https://facebook.github.io/prophet/")

