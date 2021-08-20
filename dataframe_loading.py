# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:27:48 2021

@author: Grant Isaacs
"""


#LOADING DATA----------------------------------------------------------------->
"""There are several methods avaialble for loading data. These include:
    pandas.read_csv (The most robust and flexible of these options.)
    numpy.loadtxt
    numpy.genfromtxt
    manual loading
    pickles
"""



#IMPORT LIBRARIES------------------------------------------------------------->
import numpy as np
import pandas as pd
import pickle




#LOAD DATA-------------------------------------------------------------------->
"""This data set can be located at:
    https://www.kaggle.com/ronitf/heart-disease-uci
"""
filename = "heart_disease.csv"




#PANDAS METHOD---------------------------------------------------------------->
pandas_dataset = pd.read_csv(filename)
pandas_dataset.head()




#NUMPY METHODS---------------------------------------------------------------->
numpy_dataset_01 = np.loadtxt(filename, delimiter = ",", skiprows=1)
numpy_dataset_02 = np.genfromtxt(filename, delimiter = ",", dtype=None, names=True, encoding="utf-8-sig")




#MANUAL LOADING--------------------------------------------------------------->
def load_file(filename):
    with open(filename, encoding="utf-8-sig") as f:
        data, cols = [], []
        for i, line in enumerate(f.read().splitlines()):
            if i == 0:
                cols += line.split(",")
            else:
                data.append([float(x) for x in line.split(",")])
        
        df = pd.DataFrame(data, columns=cols)
    return df

load_file(filename)




#PICKLES---------------------------------------------------------------------->
"""Use caution when utilizing Python's built in pickle method. Changes may
occur that deprecates old versions of the function that may impact how your
data is saved and loaded.

When using pandas, the best practice is to use the pandas implementation of 
pickle to ensure as much future functionality as possible. However,
deprecation may occur in the future.

USE PICKLE WITH CAUTION!"""

"""The Pandas implementation of pickle:
    df.to_pickle
    df.read_pickle
"""

