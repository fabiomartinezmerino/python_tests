#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 19:39:50 2018

@author: Alicia
"""

def array_leaders(numbers):
    result_array = []
    for counter in range(0,len(numbers)-1,1):
        if numbers[counter] > sum (numbers[counter+1:]):
            result_array.append(numbers[counter])
    if numbers[len(numbers)-1] > 0:
        result_array.append(numbers[len(numbers)-1])
    return result_array
print(array_leaders([0,-1,-29,3,2]))