#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:25:08 2018

@author: Alicia
"""

def pofi(n):
    #index_of_result = n%4
    results = ["1","i","-1","-i"]
    return results[n%4]




print(pofi(10))