#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 19:43:10 2018

@author: Alicia
"""

def reverse_number(n):
    intermediate_string = str(abs(n))
    
    result_string=""
    offset = len(intermediate_string)-1
    for i in range(0,offset+1):
        result_string += intermediate_string[offset-i]
    
    if n<0:
        return (-1*int(result_string)   )
    else:
        return (int(result_string))

print("El resultado es:" , reverse_number(833332197))