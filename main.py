import matplotlib.pyplot as plt
#import matplotlib as mpl
import os
import pandas as pd

# Merge Sales data into a single file sales_merged.csv

df = pd.read_csv('Sales-data/Sales_January_2019.csv')
sales_merged = pd.DataFrame()

files = [file for file in os.listdir(r'c:\Users\lzabo\PycharmProjects\Data-tasks-with-Pandas\Sales-data')]

for file in files:
    df = pd.read_csv(r"c:\Users\lzabo\PycharmProjects\Data-tasks-with-Pandas\Sales-data\\" + file)
    sales_merged = pd.concat([sales_merged, df])

sales_merged.to_csv("sales_merged.csv", index=False)
all_sales_merged = pd.read_csv("sales_merged.csv")

# What was the best month for sales? How much was earned that month?

# Clean NaN in column Order Date
nan_df = all_sales_merged[all_sales_merged.isna().any(axis=1)]
all_sales_merged = all_sales_merged.dropna(how="all")

# Clean column Order Date from "Or" (error: invalid literal for int() with base 10: 'Or')
all_sales_merged = all_sales_merged[all_sales_merged['Order Date'].str[0:2] != 'Or']

# Clean columns Quantity Ordered and Price Each. Converting to the correct type
all_sales_merged['Quantity Ordered'] = pd.to_numeric(all_sales_merged['Quantity Ordered'])  # convert to int
all_sales_merged['Price Each'] = pd.to_numeric(all_sales_merged['Price Each'])  # convert to float

# Add Month column
all_sales_merged['Month'] = all_sales_merged['Order Date'].str[0:2]
all_sales_merged['Month'] = all_sales_merged['Month'].astype('int32')

# Add Sales column
all_sales_merged['Sales'] = all_sales_merged['Quantity Ordered'] * all_sales_merged['Price Each']

best_month_for_sales = all_sales_merged.groupby(['Month']).sum()
best_month_for_sales = best_month_for_sales[['Sales']]
print(best_month_for_sales)


# Plotting the answer "What was the best month for sales? How much was earned that month?"
months = range(1, 13)
best_month_for_sales.plot()
plt.bar(months, best_month_for_sales['Sales'])
plt.xticks(months)
plt.xlabel('Month number')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.show()

