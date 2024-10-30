# -*- coding: utf-8 -*-
"""automobile.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/119RzcbupqE9Vo4wxYnlHyUTbd0ABOdnY
"""

import pandas as pd
import numpy as np

filepath="/content/automobile.csv"
auto_df=pd.read_csv(filepath)
auto_df

auto_df.columns

auto_df.head()

auto_df.tail()

auto_df.info()

auto_df.replace('?', np.nan, inplace=True)  # replace '?' with NaN

import seaborn as sns

sns.heatmap(auto_df.isna())

# drop rows with missing values in the price column
auto_df.dropna(subset=['price'], axis=0, inplace=True)

# replace missing values in normalized-losses column with mean value
auto_df['normalized-losses'].fillna(auto_df['normalized-losses'].astype(float).mean(), inplace=True)

auto_df.dtypes

# Convert data types from object to float
auto_df[['normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm', 'price']] = auto_df[['normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm', 'price']].astype(float)

auto_df.dtypes

# Check for duplicates
auto_df.drop_duplicates(inplace=True)

auto_df

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a box plot of the price feature
sns.boxplot(x="price", data=auto_df)

# Display the plot
plt.show()

# Dealing with outliers
auto_df = auto_df[(auto_df['price'] >= auto_df['price'].quantile(0.05)) &
        (auto_df['price'] <= auto_df['price'].quantile(0.95))]

auto_df.info()

# Histogram of city-mpg:

sns.histplot(auto_df['price'], kde=True, color='skyblue', bins=20)

# Scatterplot of horsepower vs. price colored by fuel-type:

sns.scatterplot(x='horsepower', y='price', hue='fuel-type', data=auto_df)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have already loaded your data into auto_df

# Convert numeric columns to appropriate types
numeric_columns = auto_df.select_dtypes(include=['float64', 'int64']).columns

# Plot correlation heatmap for numeric columns only
plt.figure(figsize=(15, 10))
sns.heatmap(auto_df[numeric_columns].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Boxplot of price vs. body-style:
sns.boxplot(x='body-style', y='price', data=auto_df)









