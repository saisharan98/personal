# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:56:58 2021

@author: Sai
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filepath = 'D:/Sai Sharan Sundar/personalprojects/regression/data/prices.csv'
data_read = pd.read_csv(filepath)
prices = data_read.copy()
print(prices[0])

plt.figure(1)
