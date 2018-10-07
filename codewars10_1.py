#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:11:37 2018

@author: Alicia
"""

def reverse_number(n):
    if n:
        my_string=str(abs(n))
        my_string=my_string[::-1]
        return int((n/abs(n))*int(my_string))
    else:
        return n

print(reverse_number(0))