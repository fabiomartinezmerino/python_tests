#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:52:18 2018

@author: Alicia
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    # we make first argument to be smaller or equal than second
    if a > b:
        return gcdIter(b,a)
    else:
        tempt_gcd = a
        while True:
            if (a%tempt_gcd == 0 and b%tempt_gcd == 0) or tempt_gcd == 1:
                return tempt_gcd
            else:
                tempt_gcd-=1
    
print(gcdIter(56,35))