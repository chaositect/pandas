# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:17:56 2021

@author: Grant Isaacs
"""

#IMPORT LIBRARIES------------------------------------------------------------->
import numpy as np
import pandas as pd



#LOAD DATA-------------------------------------------------------------------->
"""This data set can be located at:
    https://www.kaggle.com/ronitf/heart-disease-uci
"""
dataset = pd.read_csv("heart_disease.csv")
random_data = np.random.random(size = (5,3))




#CONVERSIONS------------------------------------------------------------------>
"""Convert a pandas dataframe into a numpy array."""
np_dataset_01 = dataset.to_numpy()

"""Referencing the .values attribute works but may be deprecated in the future."""
np_dataset_02 = dataset.values




#COPYING A NUMPY ARRAY-------------------------------------------------------->
""".copy ensures you have copied the dataframe and haven't created a reference."""
np_dataset_03 = dataset.to_numpy().copy()




#CREATING PANDAS DATAFRAMES--------------------------------------------------->
"""From a numpy array..."""
pd_dataset_01 = pd.DataFrame(data = random_data, columns = ["A", "B", "C"])

"""From a dictionary..."""
pd_dataset_02 = pd.DataFrame(data={"A":[1, 2, 3], "B":[4, 5, 6], "C":[7, 8, 9]})

"From a numpy structured array..."
dtype = [("A", np.int), ("B", (np.str, 20))]
data = np.array([(1, "Sam"), (2, "Alex"), (3, "John")], dtype = dtype)
pd_dataset_03 = pd.DataFrame(data)




#SAVING A DATAFRAME----------------------------------------------------------->
"""The most efficient way to save a data frame is with the to_csv method.
From this method you can specify whether or not to include the index as well as 
specifying the formatting of float data types."""
dataset.to_csv("exported_data.csv", index=False, float_format="%0.4f")

"""APickling is faster but has a greater probability of breaking."""
dataset.to_pickle("pickled_set.pkl")
pickle_dataset = pd.read_pickle("pickled_set.pkl")




#INSPECTING DATAFRAMES-------------------------------------------------------->
""".head loads the first five rows of the data frame by default.
A parameter specifying the number of rows to return can be provided."""
print(dataset.head(10))

""".tail functions the same way as .head but pulls from the bottom of the dataset."""
print(dataset.tail(20))

""".sample will pull a random number of samples from the dataframe.
If replace is set to True sampling is done with replacement."""
print(dataset.sample(15, replace=False))

""".info will provide information about the dataframe."""
test_null = pd.read_csv("heart_disease_nulls.csv")
print(dataset.info())
print(test_null.info())

""".describe provides information on the dataframe's columns and related metrics."""
print(dataset.describe())

""".shape provides the dimensions of the dataframe."""
print(dataset.shape)

""".corr shows correlations between the features of the dataframe."""
print(dataset.corr())

""".value_counts is used to count the occurence of a value in a column."""
print(dataset['age'].value_counts())

""".max and .min provides the max and min for each column."""
print(dataset.max())
print(dataset.min())

""".unique returns all of the unique values in a column."""
print(dataset["age"].unique())
print(dataset.age.unique())
