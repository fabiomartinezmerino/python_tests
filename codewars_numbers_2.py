#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:12:28 2018

@author: Alicia
"""
import math
def balanced_num(number):
    digit_list = [int(x) for x in str(number)]
    left_sum = 0
    right_sum = 0
    
    if len(digit_list) == 1 or len(digit_list) == 2: #balanced by definition
        return "Balanced"
    
    elif len(digit_list)%2 ==0: #even number of digits
        for index in range(0,int(len(digit_list)/2)-1):
            left_sum += int(digit_list[index])
        for index in range(int(len(digit_list)/2)+1,len(digit_list)):
            right_sum += int(digit_list[index])
        
    else:#odd number of digits
       
       print("left sum= " + str(left_sum))
       print("right sum= " + str(right_sum))
       
       print("Hasta: " + str(math.floor(len(digit_list)/2)))
       
       for index in range(0,math.floor(len(digit_list)/2)):
           left_sum += (int(digit_list[index]))
       
       print("Desde: " + str(math.ceil(len(digit_list)/2))) 
       for index in range(math.ceil(len(digit_list)/2),len(digit_list)):
           right_sum += (int(digit_list[index]))
          
    if right_sum == left_sum:
            return "Balanced"
    else:
            return " Not Balanced"
        
print(balanced_num(432))
            