# Stock_Price_Analysis
Python program to perform stock price analysis using flask for web application development.

Author: Siddhant Mahajani

Main Program: app.py - Program to execute stock analysis.
The application is executed on: http://localhost:7077/

Input required: Ticker symbol of the company whose stock needs to be analysed.
Output: Grapahical representation of the companies stock price.

company.py - Program used to fetch Company Name of the Ticker submitted.

stock_analysis.py - Program used to perform companies stock analysis and visualise result.

Libraries used:<br/>
yfinance: Yahoo Finance library to get data about companies stocks.<br/>
plotly: To visualise the data.<br/>
pandas: To read data from csv and filter out results.<br/>
flask: To get input from website and display graph on the browser<br/>

To install the libraries use pip install <library_name> i.e. pip install pandas.
