# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:15:19 2021

@author: Grant Isaacs
"""

#IMPORT LIBRARIES------------------------------------------------------------->
import pandas as pd




#LOAD DATA-------------------------------------------------------------------->
"""This data set can be located at:
    https://www.kaggle.com/ronitf/heart-disease-uci
"""
dataset = pd.read_csv("heart_disease.csv")




#BAR PLOTS-------------------------------------------------------------------->
"""Group the data into bins and then call the chart."""
cp = dataset.groupby(by = 'cp').median().reset_index()
cp.plot.bar(x='cp', y='age')




#SCATTER PLOTS---------------------------------------------------------------->
dataset.plot.scatter("age", "trestbps")




#LINE PLOTS------------------------------------------------------------------->
"""Group the data by feature and then call one or more additional measures."""
ages = dataset.groupby("age").median().reset_index()
ages.plot.line("age", ["chol", "trestbps"])




#HISTOGRAMS------------------------------------------------------------------->
"""By default the data is split into 10 bins.
This can be adjusted via the bins parameter."""
dataset.age.plot.hist(bins = 30)




#BOX PLOTS-------------------------------------------------------------------->
dataset[['trestbps', 'thalach']].plot.box()




#HEXBINS---------------------------------------------------------------------->
"""Hexbin parameters:
    vmax sets the range of the color bar
    gridsize sets the dimensions of the grid
    line width determines the amount of overlap between the data points."""
dataset.plot.hexbin(x = 'chol', y = 'age', vmax = 5, gridsize=25, linewidth=0.25)