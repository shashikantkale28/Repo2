# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:15:49 2022

@author: Admin
"""

import pandas as pd
import numpy as np

import os

os.chdir('D:\Machine Learnng\Toyota')


cardata=pd.read_csv('Toyota.csv', index_col=0)


df1=cardata.copy()

index1=df1.index

columns1=df1.columns


df1.shape
df1.ndim


df1.head(6)
df1.tail(5)

df1.at[3,'FuelType']
df1.iat[4,4]

df1.loc[1,'FuelType']


df1.dtypes


df1.get('FuelType')


df1.dtypes.value_counts()


df1.select_dtypes( exclude='object')


df1.info()

print(np.unique('Age'))














