# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:29:53 2020

@author: LukaszMalucha
"""

import yfinance as yf
import pandas as pd


def insert_column_value_from_dictionary(dictionary, string):
    """Helper function that unpacks metadata dict to columns"""
    for key, value in dictionary.items():
        if key == string:
            return value
        
        
def add_column_for_key(dataset, keys):
    """Helper funciton that creates column for each key"""
    for key in keys:
        dataset[key] = ""
    return dataset        
        


column_list = ['payoutRatio','trailingAnnualDividendRate','dividendRate','exDividendDate',
               'beta','trailingPE','priceToSalesTrailing12Months','forwardPE',
               'dividendYield','enterpriseToRevenue','profitMargins','enterpriseToEbitda',
               'forwardEps','trailingEps','priceToBook','enterpriseValue','earningsQuarterlyGrowth',
               'pegRatio', 'longName', 'symbol']


dataset = pd.DataFrame(columns=column_list)


string = "AAXN,AIR,AIRI,AJRD,AOBC,ASTC,ATRO,AVAV,BA,CODA,CUB,CVU,CW,DCO,ERJ,ESE,ESLT,FLIR,GD,GE,HEI,HEI.A,HII,HXL,ISSC,KAMN,KTOS,KVHI,LHX,LMT,MAGS,MAXR,MOG.A,MOG.B,MSI,NOC,PKE,RADA,RTX,SIF,SPCE,SPR,SSTI,TATT,TDG,TDY,TGI,TXT,UAVS"
stocks = string.split(",")



for stock in stocks:
    try:
        info = yf.Ticker(stock).info
        dataset = dataset.append(info, ignore_index=True )  
    except:
        pass














yf.Ticker("MSFT").info






    
    
  
  