#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:10:33 2018

@author: Alicia
"""
def round_to_next5(n):
    # Round to next (higher) multiple of 5
    if n%5 == 0:
        pass
    else:
        while True:
            n = n +1
            if n%5 == 0:
                break

    return n

print (round_to_next5(10))
