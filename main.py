import os

import pandas as pd

# Merge Sales data into a single file sales_merged.csv

df = pd.read_csv('Sales-data/Sales_January_2019.csv')
print(df.head())

sales_merged = pd.DataFrame()

files = [file for file in os.listdir(r'c:\Users\lzabo\PycharmProjects\Data-tasks-with-Pandas\Sales-data')]

for file in files:
    df = pd.read_csv(r"c:\Users\lzabo\PycharmProjects\Data-tasks-with-Pandas\Sales-data\\" + file)
    sales_merged = pd.concat([sales_merged, df])

sales_merged.to_csv("sales_merged.csv", index=False)
