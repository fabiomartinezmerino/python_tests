#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 19:34:14 2018

@author: Alicia
"""
import itertools
#import operator
def min_sum(arr):
    # Your code here
    my_list_of_products = []
    
    for pairmultiply in itertools.permutations(arr,len(arr)):
        sumbuf=0
        for i in range(0,len(arr),2):
            sumbuf+=(pairmultiply[i]*pairmultiply[i+1])
        my_list_of_products.append(sumbuf)
    my_list_of_products = set(my_list_of_products)
    

    print(my_list_of_products)
    

    return min(sorted(set(my_list_of_products)))
    
   

print(min_sum([12,6,10,26,3,24]))