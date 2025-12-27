# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Create DataFrame
path = 'data/automobileEDA.csv'
df = pd.read_csv(path)

# Print DataFrame headers
print(df.head())

## Analyzing Individual Features (Columns) Patterns Using Visualization

# List the data types for each column
print(df.dtypes)
print('peak-rpm data type:',df['peak-rpm'].dtype)

# We can calculate the correlation between variables of type 'int64' or 'float64' using method 'corr'
print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())

# Positive Linear Relationship

# Engine size as potential predictor variable of price
sns.regplot(x='engine-size', y='price', data=df)
plt.ylim(0,)
plt.show()

# As the engine-size goes up, the price goes up: this indicates a positive direct correlation between these two variables.
# Engine size seems like a pretty good predictor of price since the regression line is almost a perfect diagonal line.

engine_size_price_correlation = df[['engine-size', 'price']].corr()
print(engine_size_price_correlation)

sns.regplot(x='highway-mpg', y='price', data=df)
plt.ylim(0,)
plt.show()

# As highway-mpg goes up, the price goes down: this indicates an inverse/negative relationship between these two variables.
# Highway mpg could potentially be a predictor of price.

high_mpg_price_correlation = df[['highway-mpg', 'price']].corr()
print(high_mpg_price_correlation)

# Weak Linear Relationship

sns.regplot(x='peak-rpm', y='price', data=df)
plt.ylim(0,)
plt.show()

# Peak rpm does not seem like a good predictor of the price at all since the regression line is close to horizontal.
# Also, the data points are very scattered and far from the fitted line, showing lots of variability. Therefore, it's
# not a reliable variable.

peak_rpm_price_correlation = df[['peak-rpm', 'price']].corr()
print(peak_rpm_price_correlation)

sns.regplot(x='stroke', y='price', data=df)
plt.ylim(0,)
plt.show()

stroke_price_correlation = df[['stroke', 'price']].corr()
print(stroke_price_correlation)

# There is a weak correlation

# Categorical Variables

# These are variables that describe a 'characteristic' of a data unit, and are selected from a small group of categories.
# The categorical variables can have the type "object" or "int64". A good way to visualize categorical variables is by using boxplots.

# Relationship between 'body-style' and 'price'
sns.boxplot(x='body-style', y='price', data=df)
plt.ylim(0,)
plt.show()

sns.boxplot(x='engine-location', y='price', data=df)
plt.ylim(0,)
plt.show()

sns.boxplot(x='drive-wheels', y='price', data=df)
plt.ylim(0,)
plt.show()

# Descriptive Statistical Analysis

# The describe function automatically computes basic statistics for all continuous variables. Any NaN values are
# automatically skipped in these statistics.

# This will show:
#
# the count of that variable
# the mean
# the standard deviation (std)
# the minimum value
# the IQR (Interquartile Range: 25%, 50% and 75%)
# the maximum value

print(df.describe())

# The default setting of "describe" skips variables of type object. We can apply the method "describe" on the variables of type 'object' as follows:
# df.describe(include=['object']

# Value Counts

# Value counts is a good way of understanding how many units of each characteristic/variable we have. We can apply the
# "value_counts" method on the column "drive-wheels". Don’t forget the method "value_counts" only works on pandas series,
# not pandas dataframes. As a result, we only include one bracket df['drive-wheels'], not two brackets df[['drive-wheels']].

print(df['drive-wheels'].value_counts())

print(df['drive-wheels'].value_counts().to_frame())

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
print(drive_wheels_counts)

drive_wheels_counts.index.name = 'drive-wheels'
print(drive_wheels_counts)

# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
print(engine_loc_counts.head(10))

# Basics of Grouping

# The "groupby" method groups data by different categories. The data is grouped based on one or several variables, and
# analysis is performed on the individual groups.
#
# For example, let's group by the variable "drive-wheels". We see that there are 3 different categories of drive wheels.

print(df['drive-wheels'].unique())

df_group_one = df[['drive-wheels','body-style','price']]

# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
print(df_group_one)


# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(grouped_test1)


grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
print(grouped_pivot)

grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
print(grouped_pivot)

# grouping results
df_gptest2 = df[['body-style','price']]
grouped_test_bodystyle = df_gptest2.groupby(['body-style'],as_index= False).mean()
print(grouped_test_bodystyle)

# Variables: Drive Wheels and Body Style vs. Price

#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()


fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()

# Correlation and Causation
#
# Correlation: a measure of the extent of interdependence between variables.
#
# Causation: the relationship between cause and effect between two variables.
#
# It is important to know the difference between these two. Correlation does not imply causation.
# Determining correlation is much simpler the determining causation as causation may require independent experimentation.

# Wheel-Base vs. Price
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# Horsepower vs. Price
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Length vs. Price
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Width vs. Price
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )

# Curb-Weight vs. Price
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Engine-Size vs. Price
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# Bore vs. Price
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value )

# City-mpg vs. Price
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Highway-mpg vs. Price
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value )

# ANOVA: Analysis of Variance
# The Analysis of Variance (ANOVA) is a statistical method used to test whether there are significant differences between the means of two or more groups. ANOVA returns two parameters:
#
# F-test score: ANOVA assumes the means of all groups are the same, calculates how much the actual means deviate from the assumption, and reports it as the F-test score. A larger score means there is a larger difference between the means.
#
# P-value: P-value tells how statistically significant our calculated score value is.
#
# If our price variable is strongly correlated with the variable we are analyzing, we expect ANOVA to return a sizeable
# F-test score and a small p-value.

grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)
print(df_gptest)

print(grouped_test2.get_group('4wd')['price'])

# ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'],
                              grouped_test2.get_group('4wd')['price'])

print("ANOVA results: F=", f_val, ", P =", p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])

print("ANOVA results: F=", f_val, ", P =", p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])

print("ANOVA results: F=", f_val, ", P =", p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])

print("ANOVA results: F=", f_val, ", P =", p_val)





