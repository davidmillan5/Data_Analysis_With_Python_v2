# Import pandas
import pandas as pd
import numpy as np
import matplotlib as plt

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Create a Python list headers containing name of headers.

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# Loading dataset to create a dataFrame
path = 'data/imports-data-85.csv'
autos = pd.read_csv(path, names=headers)

# Show first 5 rows
autos_headers = autos.head()
print(autos_headers)

#So, how do we identify all those missing values and deal with them?
#How to work with missing data?
#Steps for working with missing data:
#1. Identify missing data
#2. Deal with missing data
#3. Correct data format


# Identify and handle missing values

## Convert "?" to NaN
autos.replace("?", np.nan, inplace=True)
print(autos.head())

## Evaluating for Missing Data
missing_data = autos.isnull()
print(missing_data.head(5))

## Count Missing values in Each Column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print('')

# Calculate the mean value for the "normalized-losses" column
avg_norm_loss = autos['normalized-losses'].astype(float).mean(axis=0)
print("Average of normalized-losses:",avg_norm_loss)

# Replace "NaN" with mean value in "normalized-losses" column
autos['normalized-losses'].replace(np.nan, avg_norm_loss, inplace=True)

# Calculate the mean value for the "stroke" column
avg_stroke = autos['stroke'].astype(float).mean(axis=0)
print("Average of stroke:", avg_stroke)

# Replace "NaN" with the mean value in the "stroke" column
autos['stroke'].replace(np.nan, avg_stroke, inplace=True)

# Calculate the mean value for the "bore" column
avg_bore = autos['bore'].astype(float).mean(axis=0)
print("Average of bore:",avg_bore)

# Replace "NaN" with the mean value in the "bore" column
autos['bore'].replace(np.nan, avg_bore, inplace=True)

# Calculate the mean value for the "horsepower" column
avg_horsepower = autos['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)

# Replace "NaN" with the mean value in the "horsepower" column
autos['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

# Calculate the mean value for "peak-rpm" column
avg_peakrpm= autos['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)

# Replace "NaN" with the mean value in the "peak-rpm" column
autos['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# To see which values are present in a particular column, we can use the ".value_counts()" method:
autos['num-of-doors'].value_counts()

# You can see that four doors is the most common type. We can also use the ".idxmax()" method to calculate the most common type automatically:
autos['num-of-doors'].value_counts().idxmax()

#replace the missing 'num-of-doors' values by the most frequent
autos["num-of-doors"].replace(np.nan, "four", inplace=True)

# simply drop whole row with NaN in "price" column
autos.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
autos.reset_index(drop=True, inplace=True)

print(autos.head())

print(autos.dtypes)

# Convert data types to proper format

autos[["bore", "stroke"]] = autos[["bore", "stroke"]].astype("float")
autos[["normalized-losses"]] = autos[["normalized-losses"]].astype("int")
autos[["price"]] = autos[["price"]].astype("float")
autos[["peak-rpm"]] = autos[["peak-rpm"]].astype("float")

print(autos.dtypes)

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
autos['city-L/100km'] = 235/autos["city-mpg"]

# check your transformed data
print(autos.head())

autos.rename(columns={"highway-mpg": "highway-L/100km"}, inplace=True)
autos['highway-L/100km'] = 235/autos["highway-L/100km"]

# check your transformed data
print(autos.head())


# Data Normalization

# replace (original value) by (original value)/(maximum value)
autos['length'] = autos['length']/autos['length'].max()
autos['width'] = autos['width']/autos['width'].max()

autos['height'] = autos['height']/autos['height'].max()

# show the scaled columns
autos[["length","width","height"]].head()

## Binning

autos["horsepower"]= autos["horsepower"].astype(int, copy=True)

# matplotlib inline

from matplotlib import pyplot
plt.pyplot.hist(autos["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


bins = np.linspace(min(autos["horsepower"]), max(autos["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']

autos['horsepower-binned'] = pd.cut(autos['horsepower'], bins, labels=group_names, include_lowest=True )
autos[['horsepower','horsepower-binned']].head(20)

autos["horsepower-binned"].value_counts()

pyplot.bar(group_names, autos["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

# draw histogram of attribute "horsepower" with bins = 3
plt.pyplot.hist(autos["horsepower"], bins = 3)

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

dummy_variable_1 = pd.get_dummies(autos["fuel-type"])
dummy_variable_1.head()

dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
dummy_variable_1.head()

# merge data frame "df" and "dummy_variable_1"
autos = pd.concat([autos, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
autos.drop("fuel-type", axis = 1, inplace=True)

# get indicator variables of aspiration and assign it to data frame "dummy_variable_2"
dummy_variable_2 = pd.get_dummies(autos['aspiration'])

# change column names for clarity
dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)

# show first 5 instances of data frame "dummy_variable_1"
print(dummy_variable_2.head())

# merge the new dataframe to the original dataframe
autos = pd.concat([autos, dummy_variable_2], axis=1)

# drop original column "aspiration" from "df"
autos.drop('aspiration', axis = 1, inplace=True)

print(autos.head())

autos.to_csv('clean_df.csv')