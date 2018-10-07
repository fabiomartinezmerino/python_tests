#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:59:21 2018

@author: Alicia
"""

"""
read a file words.txt and prints the content in uppercase
"""
try:
    file_name = input("Please write absolute file path:\n")
    file_handler = open(file_name,"r")
    for line in file_handler:
        print(line.upper())
except:
    print("problems with file ")
    