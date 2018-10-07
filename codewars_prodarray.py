#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:46:20 2018

@author: Alicia
"""
import operator
import functools






def product_array(numbers):
    """
    numbers:list of positive integers
    returns: list of numbers built up from product from every item in previous list except the
    one corresponidng to the ith element
    """
    
    print(numbers)
    returned_list = []
    for counter in range(0,len(numbers)):
        buffer_list = numbers.copy()
        print(buffer_list)
        del(buffer_list[counter])
        returned_list.append(functools.reduce(operator.mul, buffer_list))
    return returned_list
        
    
print(product_array([16,17,4,3,5,2]))