# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:07:01 2021

@author: Grant Isaacs
"""

#IMPORT LIBRARIES------------------------------------------------------------->
import pandas as pd




#LOAD DATA-------------------------------------------------------------------->
"""The data can be located at:
    https://www.kaggle.com/c/rossmann-store-sales/data
"""
dataset = pd.read_csv("train.csv", low_memory=False, parse_dates=["Date"])




#GROUPING--------------------------------------------------------------------->
"""Using the group by creates a group object upon which various methods can be called."""
dataset_01 = dataset.groupby("Store")
dataset_01 = dataset_01.mean()
dataset_01 = dataset_01.reset_index()

dataset_02 = dataset.groupby(["Store", "DayOfWeek"], as_index = False).sum()




#CONTINUOUS GROUPING---------------------------------------------------------->
"""The first step in grouping continuous data is to determine where to stop each bin."""
dataset_03 = dataset.copy()
print(dataset_03.Sales.describe())
bins = [0, 2000, 4000, 6000, 8000, 10000, 50000]
cuts = pd.cut(dataset_03.Sales, bins, include_lowest = True)
dataset_03["SalesGroup"] = cuts
print(dataset_03.head())
dataset_04 = dataset_03.groupby(["Store", "SalesGroup", "DayOfWeek"]).Sales.count()




#AGGREGATION------------------------------------------------------------------>
"""Single aggregates require a single call to apply to the whole dataframe."""
dataset_05 = dataset.groupby("Store")
dataset_05 = dataset_05.mean()

"""Multiple aggregates call different calculations on different fields.
Call the .agg function and pass in a dictionary of columns and functions."""
dataset_06 = dataset.groupby(["Store", "DayOfWeek"], as_index = False).agg({"Sales":"mean", "Customers":'count'})

"""Complexity can be increased by providing a list for a given dictionary key to perform multiple calculations.
User defined functions can also be supplied in the dictionaries."""
dataset_07 = dataset.groupby(["Store", "DayOfWeek"], as_index = False).agg({"Sales":["mean", "min", "max"], "Customers":'count'})
