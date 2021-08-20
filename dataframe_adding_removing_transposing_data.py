# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 16:59:12 2021

@author: Grant Isaacs
"""

#IMPORT LIBRARIES------------------------------------------------------------->
import pandas as pd




#LOAD DATA-------------------------------------------------------------------->
"""The data can be located at:
    https://www.kaggle.com/nasa/astronaut-yearbook
"""
dataset = pd.read_csv("astronauts.csv")




#MODIFYING DATA TYPE---------------------------------------------------------->
"""To convert a column's data type apply the conversion and reassign to the same column."""
dataset_01 = dataset.copy()
dataset_01['Birth Date'] = pd.to_datetime(dataset['Birth Date'], format = "%m/%d/%Y")
print(dataset_01['Birth Date'].dt.year)




#CATEGORICALS----------------------------------------------------------------->
dataset_02 = dataset.copy()
dataset_02['Military Rank'] = dataset_02['Military Rank'].astype("category")




#NUMERIC AND STRING CONVERSION------------------------------------------------>
dataset_02['Convert_Me'] = float(5.0)
print(dataset_02['Convert_Me'].dtype)
dataset_02['Convert_Me']= dataset_02['Convert_Me'].astype("str")
print(dataset_02['Convert_Me'].dtype)
dataset_02['Convert_Me']= dataset_02['Convert_Me'].astype("float")
print(dataset_02['Convert_Me'].dtype)
dataset_02['Convert_Me']= dataset_02['Convert_Me'].astype("int")
print(dataset_02['Convert_Me'].dtype)




#REMOVING COLUMNS OR ROWS----------------------------------------------------->
"""To drop a column use the .drop method and specify axis = 1."""
dataset_03 = dataset.drop(["Name", "Group"], axis=1)
dataset_03 = dataset.drop(columns=["Name", "Group"], axis=1)

"""To Drop a row you specify the index and set the axis = 0.
Doing so does not reset the index."""
dataset_03 = dataset.drop(1, axis = 0)
dataset_03 = dataset.drop(range(0, 300), axis = 0)
dataset_03 = dataset.drop([310, 325, 350], axis = 0)




#ADDING ROWS------------------------------------------------------------------>
""".append adds a row.
The new row can be in the form of a dictionary, a list of lists, or another dataframe."""
dataset_04 = dataset.copy()
dataset_04 = dataset_04.append({"Name": "Grant Isaacs", "Year": 2021}, ignore_index=True)
dataset_04 = dataset_04.append([["The New Guy", 2010], ["His Brother", 2020]], ignore_index=True)
dataset_05 = dataset.append(dataset)




#ADDING COLUMNS--------------------------------------------------------------->
"""To add a column, reference the column as if it already exists."""
dataset_05["New Data"] = "This is the new data to be copied into every observation."

"""Alternatively the assign method can be used."""
dataset_05 = dataset_05.assign(some_col="some_val")

"""If you wish to specify the location of the new column within the dataframe, .insert is used."""
dataset_05.insert(0, "First_Name", dataset_05.Name.str.split(" ", 1, expand=True)[0])




#TRANSPOSING THE DATAFRAME---------------------------------------------------->
"""When transposing it is often a good idea to set a new index to act as the column names for the new dataframe.
To transpose, use .T"""
dataset_06 = dataset.copy()
dataset_06 = dataset_06.set_index("Name")
dataset_06 = dataset_06.T
