#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 22:45:45 2018

@author: Alicia
"""
#import math as m
def is_narcissistic(i):
    intermediate_string = str(i)
    narcissistic_result = 0
    length_of_number = len(intermediate_string)
    for char_number in intermediate_string:
        narcissistic_result += pow(int(char_number),length_of_number)
    if i == narcissistic_result:
        return True
    else:
        return False



print(is_narcissistic(153))