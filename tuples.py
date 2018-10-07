#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:27:30 2018

@author: Alicia
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[1::2]
print(oddTuples([1,2,3,4,5,6]))