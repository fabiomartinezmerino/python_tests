#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:34:29 2018

@author: Alicia
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    
    '''
    # we will understand a < b
    # we are going to use euclides' algorithm
    
    if b < a:
        print("We switch a, b so first argument is smaller")
        return gcdRecur(b,a)
    else:
        print("Arguments are in correct order, first %d, then %d" % (a,b))
        if b%a == 0:
            print ("First argument %d is GCD" % (a))
            return a
        else:
            print ("we need to recursive call GCD with arguments %d, %d" % \
                   (a, b%a))
            return gcdRecur(a,b%a)
        
            
            
print(gcdRecur(56,35))          