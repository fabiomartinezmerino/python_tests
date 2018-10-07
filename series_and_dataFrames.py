#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 22:41:40 2018

@author: Alicia
"""
"""
Pandas Series use
Create a Series from a dictionary containning student name subject and grade
Create a DataFrame from previous Series indexing by Course
"""

import numpy as np

import pandas as pd

student_series_1 = pd.Series({"Name":"Jhon", "Subject":"English", "Grade":10})

#print(student_series_1) 

print(student_series_1.index)

student_series_2 = pd.Series({"Name":"Lisa", "Subject":"English", "Grade":8})

student_series_3 = pd.Series({"Name":"Mario", "Subject":"English", "Grade":7})

student_series_4 = pd.Series({"Name":"Stanley", "Subject":"Math", "Grade":6})

student_series_5 = pd.Series({"Name":"Margaret", "Subject":"Math", "Grade":9})

#student_series_6 = pd.Series({"Name":"Jhon", "Subject":"Physics", "Grade":9.7})
#you can create a Series out of two lists
student_series_6 = pd.Series(["Jhon","Physics",9.7],index=["Name","Subject","Grade"])

student_frame = pd.DataFrame([student_series_1,student_series_2,student_series_3,student_series_4,student_series_5,student_series_6], index =["A","A","A","B","B","C"])

print(student_frame)

myList = list(student_frame.count())

print(myList)


