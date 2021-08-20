# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:32:48 2021

@author: Grant Isaacs
"""

#IMPORT LIBRARIES------------------------------------------------------------->
import pandas as pd
import numpy as np




#LOAD DATA-------------------------------------------------------------------->
dataset = np.round(np.random.normal(size=(4,3)), 2)
dataset = pd.DataFrame(dataset, columns=['A', 'B', 'C'])




#APPLY------------------------------------------------------------------------>
"""Used to execute a function against an entire dataframe or subset.
Functions used in this manner must be vectorized functions."""
def some_function(x):
    x = x**2
    x += 100
    return x

dataset_01 = dataset.apply(some_function)

"""A lambda expression can also be placed directly in the argument."""
dataset_02 = dataset.apply(lambda x: (x**2) + 100)

"""Apply can be used with one or more columns."""
dataset_03 = dataset.copy()
dataset_03[["A", "B"]] = dataset[["A", "B"]].apply(some_function)

dataset_04 = dataset.copy()
dataset_04.A = dataset.A.apply(some_function)




#MAP-------------------------------------------------------------------------->
"""Map is similar to apply but only runs on a series and can use dictionaries as inputs."""
series = pd.Series(["Steve Jackson", "Alex Trebek", "Jessica Rabbit", "Mark Hamill"])
series_01 = series.map({"Steve":"Steven"})
series_02 = series.map("My name is {}".format)
series_03 = series.map(lambda x: f"I am {x}")
series_04= dataset.A.map(lambda x: f"The number is {x}")




#VECTORIZED FUNCTIONS--------------------------------------------------------->
"""Pandas as Numpy have a number or built in vectorized functions."""
series_05 = series.split() #This will not work because .split is not a vectorized function
series_05 = series.str.split() #This is the correct version using the built in vectorized function.
series_05 = series.str.split(expand=True)
series.str.contains("Jackson")
series.str.upper()