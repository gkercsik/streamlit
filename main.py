import streamlit as st
from datetime import date

import yfinance as yf
#

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
	st.title('Welcome to my awesome Stock Prediction project')
	st.text('This project attempts to predict the Pice of a selected Ticker...')  


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

n_years = st.slider("Years of prediction:", 0 , 4)
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
	#st.header('The features I created')



#with model_training:
        #st.header('Time to train the model!')
        #st.text('Here you get to choose the hyperparameters of the model and see how the performance changes')

