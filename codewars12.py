#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:56:39 2018

@author: Alicia
"""

def max_number(n):
    intermediate_string = str(n)
    definitive_list = []
    for number in intermediate_string:
        definitive_list.append(number)
    definitive_list.sort(reverse=True)
    return int("".join(str(x) for x in definitive_list))
    
   
print (max_number(1214598))