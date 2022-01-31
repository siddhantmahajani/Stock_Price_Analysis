"""
Author: Siddhant Mahajani
Program: stock_analysis.py
Description: Program to perform stock analysis based on Ticker provided from tickers/data.csv
Date: 31st Jan 2022
"""

import yfinance as fin
from datetime import date, timedelta
import plotly.graph_objects as obj

import warnings

warnings.filterwarnings("ignore")


def analyseStockForCompanyTickerCode(ticker, name):
    today = date.today()

    date1 = today.strftime("%Y-%m-%d")
    end_date = date1
    date2 = date.today() - timedelta(days=5000)
    date2 = date2.strftime("%Y-%m-%d")
    start_date = date2

    data = fin.download(ticker, start=start_date, end=end_date, progress=False)
    data['Date'] = data.index
    data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    data.reset_index(drop=True, inplace=True)
    print(data.tail())

    figure = obj.Figure(data=[obj.Candlestick(x=data['Date'], open=data['Open'],
                                              high=data['High'], low=data['Low'], close=data['Close'])])
    figure.update_layout(title=name, xaxis_rangeslider_visible=False)
    figure.show()
