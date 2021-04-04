import streamlit as st
from datetime import date

import yfinance as yf

from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objects as go

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
	st.title('Welcome to my awesome Stock Prediction project')
	st.text('This project attempts to predict the Pice of a selected Stock ...')  


with dataset:
	st.header('Raw dataset Staring from: 2015-01-05')
	st.text('The raw data sourced from Yahoo Finance website...!')
	st.text('For AU Tickers type ".au" after the Ticker ie: "bhp.au"...')
	st.text('For Bitcoin or other cryptos type "-usd" ie: "btc-usd"...!')
	
Start = "2015-01-05"
Today = date.today().strftime("%Y-%m-%d")

stocks = ("btc-usd")
selected_stocks = stocks
selected_stocks = st.text_input("Select TICKER for prediction." , stocks)

n_years = st.slider("Years of prediction:", 1 , 4)
period = n_years * 365

@st.cache
def load_data(ticker):
    data = yf.download(ticker, Start, Today)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stocks)
data_load_state.text("Loading data...done!")

st.subheader('Raw data')
st.write(data.tail())

#with features:
st.header('Visualisation of the raw data...!')
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock opening price'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock closing price'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# "fig = px.line" it Plotly Express librart it is a lot simpler then "go" but not as powerfull.


#with model_training:
st.header('Time to train the model!')
st.text('Here you get to choose the hyperparameters of the model and see how the performance changes')

df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())

st.write('Forecast data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast components')
fig2 = m.plot_components(forecast)
st.write(fig2)

#Alles Gut Zu Ende Gut...!








