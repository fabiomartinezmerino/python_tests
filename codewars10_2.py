#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:23:31 2018

@author: Alicia
"""

def reverseNumber(n):
    if n < 0: 
        return -reverseNumber(-n)
    return int(str(n)[::-1])


print(reverseNumber(340))