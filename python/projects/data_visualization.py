import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import time

ticker = "AAPL"  # Change to any stock ticker (e.g., TSLA, MSFT)
data = []

plt.ion()  # Interactive mode ON
fig, ax = plt.subplots()

for i in range(20):  # Fetch data 20 times
    stock = yf.Ticker(ticker)
    price = stock.history(period="1m")["Close"].iloc[-1]
    
    data.append(price)
    ax.clear()
    ax.plot(data, label="Stock Price", color="blue")
    ax.legend()
    plt.pause(1)  # Update every second

plt.ioff()  # Turn off interactive mode
plt.show()

