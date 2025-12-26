# Import pandas
import pandas as pd
import numpy as np

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Loading dataset to create a dataFrame
path = 'data/Automobile_data.csv'
autos = pd.read_csv(path)

# Show the first 5 rows in the dataframe
autos_header = autos.head()
print(autos_header)

# Show the last 10 rows of the dataframe
autos_last_rows = autos.tail(10)
print(autos_last_rows)

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

# Show the first 10 rows
autos_any_numbers_rows = autos.head(10)
print(autos_any_numbers_rows)

# Replace the "?" symbol with NaN so the dropna() can remove missing values
autos_1 = autos.replace('?', np.nan)

# Drop missing values along the column "price"
autos = autos_1.dropna(subset=['price'], axis=0)

# Always check date types on the dataset
data_type_autos = autos.dtypes
print(data_type_autos)

# Statistical Summaries
statistical_summary_autos = autos.describe(include='all')
print(statistical_summary_autos)

# Show info about the dataframe
autos.info()



