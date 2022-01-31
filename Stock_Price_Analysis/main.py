"""
Author: Siddhant Mahajani
Program: main.py
Description: Main program to perform stock analysis
Date: 31st Jan 2022
"""

from stock_analysis import stock_analysis
from company_name import company

import warnings

warnings.filterwarnings("ignore")


def main():
    user_input = input("Enter Company Ticker for Stock Analysis: ")
    company_code = str(user_input).upper()
    company_name = company.getCompanyName(company_code)
    stock_analysis.analyseStockForCompanyTickerCode(ticker=company_code, name=company_name)


if __name__ == "__main__":
    main()
