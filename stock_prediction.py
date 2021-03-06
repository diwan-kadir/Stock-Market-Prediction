import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance 
from datetime import datetime

from sklearn.linear_model import LinearRegression as LR

company_list = ['aapl','ibm', 'nke']
c_name=["APPLE", "IBM", "Nike"]

model = {}
data = {}

for i in company_list:
    data[i] = yfinance.download(i).reset_index()

data['aapl'].head()

for i in company_list:
    plt.figure(figsize=(15, 5))
#     data[i]['Close'].plot()
    plt.plot(data[i]['Date'],data[i]['Close'])
    plt.xlabel('DATE')
    plt.ylabel('PRICE in Dollars')
    plt.title(i)

for i in company_list:
    model[i]=LR().fit(np.array(data[i].index).reshape(-1,1),data[i]['Close'])

for i in company_list:
    plt.figure(figsize=(15,5))
    plt.plot(data[i]['Date'], data[i]['Close'],linewidth='1',c='purple')
    plt.plot(data[i]['Date'], model[i].predict(np.array(data[i].index).reshape(-1,1)),linewidth='2',c='green')
    plt.xlabel('Date')
    plt.ylabel('Price in Dollars')
    plt.title(i)

for i in company_list:
  print("Accuracy or R-square value of {} Linear Regression Model is {} ".format(i,model[i].score(np.array(data[i].index).reshape(-1,1),data[i]['Close'])))
