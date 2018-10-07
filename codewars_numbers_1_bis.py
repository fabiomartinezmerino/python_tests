#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 20:39:21 2018

@author: Alicia
"""


def balanced_num(number):

    digit_list = [int(x) for x in str(number)]
    left_sum = 0
    right_sum = 0
    set_off = len(digit_list)//2
     
    
    if len(digit_list) == 1 or len(digit_list) == 2: #balanced by definition
        return "Balanced"

    if len(digit_list)%2 ==0:
        left_sum += sum(digit_list[:set_off-1])
    else:
        left_sum += sum(digit_list[:set_off])
    
    
    right_sum += sum(digit_list[set_off+1:])
    
          
    if right_sum == left_sum:
            return "Balanced"
    else:
            return " Not Balanced"
        
print(balanced_num(413224))
