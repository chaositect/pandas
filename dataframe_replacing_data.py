# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 16:02:55 2021

@author: Grant Isaacs
"""

#IMPORT LIBRARIES------------------------------------------------------------->
import pandas as pd




#LOAD DATA-------------------------------------------------------------------->
"""The data can be located at:
    https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
"""
dataset = pd.read_csv("ab_nyc_2019.csv")




#DEALING WITH NANs------------------------------------------------------------>
""".dropna removes any row with a NaN in any column."""
dataset_01 = dataset.dropna()

"""A threshold can be specified to indicate the minimum number of na's an observation is allowed to contain."""
dataset_02 = dataset.dropna(thresh=3)

"""Using subset a specific column or columns can be specified to search for na's."""
dataset_03 = dataset.dropna(subset=['last_review', 'host_name'])
print(dataset_03.info())

"""Specifying an axis will drop any column with an na."""
dataset_04 = dataset.dropna(axis=1)
print(dataset_04.info())

""".fillna will populate empty cells with a value."""
dataset_05 = dataset.fillna(0)
print(dataset_05.info())




#REPLACE---------------------------------------------------------------------->
""".replace locates the target values and replaces them with the provided value."""
dataset_06 = dataset.replace("John", "Jono")
print(dataset_06.host_name[dataset_06.host_name == "Jono"])

"""Alternatively, a dictionary may be provided to identify the replacements and their new value."""
dataset_07 = dataset.replace({"John": "Jonathon", "Brooklyn": "Brooks-ville"})
print(dataset_07[['host_name', 'neighbourhood_group']])