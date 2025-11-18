import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display_functions import display

df = pd.read_csv("C:\\Users\\User\\Downloads\\source\\chapter11\\11_data\\car20240731.csv")
display(df.head())
df = df[df['배기량']!=0]

df1 = df[df['연료']=='휘발유']
df2 = df[df['연료']=='경유']

plt.figure(figsize=(5, 3))
plt.scatter(df1['배기량'], df1['CO2배출량(g_km)'], s=3, alpha=0.5, label='Gasoline')
plt.scatter(df2['배기량'], df2['CO2배출량(g_km)'], s=3, alpha=0.5, label='Diesel')
plt.legend()
plt.xlabel('displacement')
plt.ylabel('CO2 emissions')
plt.show()

cor = df1['배기량'].corr(df1['CO2배출량(g_km)'])
print(cor)

cor = df2['배기량'].corr(df2['CO2배출량(g_km)'])
print(cor)