# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:38:22 2021

@author: Grant Isaacs
"""

#IMPORT LIBRARIES------------------------------------------------------------->
import pandas as pd




#LOAD DATA-------------------------------------------------------------------->
"""The dataset can be located at:
    https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
"""
dataset = pd.read_csv("ab_nyc_2019.csv")




#SLICING COLUMNS-------------------------------------------------------------->
"""Columns can be sliced with bracket or dot notation."""
print(dataset["price"])
print(dataset[["price", "id"]])
print(dataset.price)




#ROW FILTERING---------------------------------------------------------------->
"""Rows can be filtered with comparison operators."""
print(dataset[dataset.host_name == 'Taz'])

"""Running the comparison by itself Pandas will return a boolean mask."""
print(dataset.host_name == 'Taz')

"""A boolean mask can be used to count the number of instances in a series or dataframe."""
print((dataset.host_name == 'Taz').sum())

"""Masks can be combined to create complex filters.
& = and
| = or
~ = not
"""
quick_and_cheap = (dataset.price < 100) & (dataset.minimum_nights < 3)
print(quick_and_cheap.sum())
print(dataset[quick_and_cheap])




#FILTERING ROWS AND COLUMNS--------------------------------------------------->
""".loc filters rows and columns together."""
print(dataset.loc[dataset.price < 25, ['name', 'host_name']])

"""If you want all rows and only the specified columns..."""
print(dataset.loc[:, ["price", "id"]])

"""If you want all columns and only specific rows..."""
print(dataset.loc[dataset.price < 25, :])

""".iloc is used to filter on the index.
The first argument specifies the row index.
The second argument specifies the column index.
"""
print(dataset.iloc[1:10, :])
print(dataset.iloc[:, 5])
print(dataset.iloc[1, :])
print(dataset.iloc[:, 1])
print(dataset.iloc[:, 4:])




#MASK METHODS----------------------------------------------------------------->
""".between can be used to find numbers within a given range."""
print(dataset.loc[dataset.price.between(100, 200), 'price'])

""".isin can be used to find items in a list."""
print(dataset.loc[dataset.price.isin([100, 200, 300]), 'price'])
