#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:17:44 2018

@author: Alicia
"""

def round_to_next5(n):
    # Round to next (higher) multiple of 5
    while True:
        if n%5 ==0:
            break
        else:
            n = n+1
    return n

print (round_to_next5(-323))