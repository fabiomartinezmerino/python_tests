#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 19:09:29 2018

@author: Alicia
"""

def feast(beast, dish):
    # your code here
    if (dish[0] == beast[0]) and (dish[-1]== beast[-1]):
        return True
    else:
        return False
    
print(feast("meon","miscon"))
    