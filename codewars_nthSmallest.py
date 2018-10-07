#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 14:23:52 2018

@author: Alicia
"""

def nthSmallest(input_array,n):
    input_array.sort()
    return input_array[n-1]

print (nthSmallest([2,3,5,7,6,8,11,32,234,123],3))