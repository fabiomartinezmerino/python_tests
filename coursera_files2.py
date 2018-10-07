#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:12:10 2018

@author: Alicia
"""

"""
looks for lines starting with X-DSPAM-Confidence then looks for number and keeps it
once it hs read all the file averages the numbers summed
"""

file_name = input("Please input filename: ")
file_handler = open(file_name,"r")
mybuffer = 0
counter = 0

for line in file_handler:
    if line.startswith("X-DSPAM-Confidence:"):
        
        #print(line[line.find(":")+1:].strip())
        
        number = float(line[line.find(":")+1:].strip())
        mybuffer+=number
        counter+=1
        
             
    else:
        pass
print("{:1.12}".format(mybuffer/counter))
