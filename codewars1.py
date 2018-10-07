#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 18:35:05 2018

@author: Alicia
"""

def add_binary(a,b):
    #your code here
    #c_string = "{0:b}".format(a+b)

    
    #return c_string
    
        return bin(a+b)[2:]

print(add_binary(3,1))