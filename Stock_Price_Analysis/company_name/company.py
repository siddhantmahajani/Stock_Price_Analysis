"""
Author: Siddhant Mahajani
Program: company.py
Description: Program to fetch company name from tickers/data.csv file
Date: 31st Jan 2022
"""

import pandas as pd
import warnings

warnings.filterwarnings("ignore")


def getCompanyName(ticker_symbol):
    data = pd.read_csv("data/tickers.csv")
    data = data.loc[data["Symbol"] == ticker_symbol]
    company_values = data["Name"].values
    company_name = company_values[0]
    return company_name
