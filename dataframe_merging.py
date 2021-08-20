# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:21:02 2021

@author: Grant Isaacs
"""

#IMPORT LIBRARIES------------------------------------------------------------->
import pandas as pd




#LOAD DATA-------------------------------------------------------------------->
"""The data can be located at:
    http://tiny.cc/studcsv
"""
students = pd.read_csv("students.csv")
teachers = pd.read_csv("teachers.csv")
grades_01 = pd.read_csv("grades1.csv")
grades_02 = pd.read_csv("grades2.csv")
contacts = pd.read_csv("contact.csv")




#MERGING DATAFRAME ROWS------------------------------------------------------->
grades_01["Semester"] = 1
grades_02["Semester"] = 2

"""To merge the rows of the two dataframes we can use either concat or append."""
grades_03 = pd.concat([grades_01, grades_02])
grades_03 = grades_03.reset_index(drop=True)

grades_04 = grades_01.append(grades_02)
grades_04 = grades_04.reset_index(drop=True)




#MERGING DATAFRAME COLUMNS---------------------------------------------------->
student_grades = pd.merge(students, grades_04, left_on="id", right_on="student_id")
print(students.shape, grades_04.shape, student_grades.shape)

students_02 = students.rename({"id": "student_id"}, axis=1)
students_full = students_02.merge(contacts, on='student_id')
student_grades = pd.merge(students_full, grades_04, on='student_id')
student_grades = pd.merge(student_grades, teachers, on='course')




#JOINING---------------------------------------------------------------------->
"""Joining is done on the index of the dataframes."""
students_03 = students.copy()
students_03 = students_03.set_index("id")
contacts_01 = contacts.copy()
contacts_01 = contacts_01.set_index("student_id")
students_03 = students_03.join(contacts_01)
