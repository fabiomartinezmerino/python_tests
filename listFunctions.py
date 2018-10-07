#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 18:53:26 2018

@author: Alicia
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def squared(i):
    i=i*i
    return i

testList = [1, -4, 8, -9]

applyToEach(testList,squared) 
print (testList)