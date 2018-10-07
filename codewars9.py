#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 18:47:43 2018

@author: Alicia
"""

def sum_differences_between_products_and_LCMs(pairs):
    #your code here
    result = 0
    for pair in pairs:
        #print ("producto %", pair[0]*pair[1])
        #print ("lcm %", euclidean_lcm(pair[0],pair[1]))
        result = result + (pair[0]*pair[1]) - euclidean_lcm(pair[0],pair[1])
    return result  
def euclidean_lcm(a,b):
    if (b==0):
        return a
    else:
        return ((a*b)//basic_gcd(a,b))
def basic_gcd(a,b):
    if (b>a):
        return basic_gcd(b,a)
    else:
        if (b==0):
            return a
        else:
            if(a%b==0):
                return b
            else:
                return (basic_gcd(b,a%b))
         
    
#print (euclidean_lcm(4,5))
print (sum_differences_between_products_and_LCMs([[1,1],[0,0],[13,95]]))
    