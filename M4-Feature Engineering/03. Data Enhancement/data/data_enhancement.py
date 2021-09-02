import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/User/Documents/Strive_AI_Jun_21/M4-Feature Engineering/03. Data Enhancement/data/london_merged.csv')
# print(df)
print(df.isnull().sum())
print(df.head())