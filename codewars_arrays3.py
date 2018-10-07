#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:34:17 2018

@author: Alicia
"""

def array_leaders(numbers):

    returned_array = []
    
    for counter in range (0,len(numbers)):
       if numbers[counter] > sum(numbers[counter+1:]):
           returned_array.append(numbers[counter])
    
    return returned_array
        





print(str(array_leaders([2,3,9,4,12])))
