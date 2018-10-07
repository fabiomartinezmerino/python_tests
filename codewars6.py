#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:46:24 2018

@author: Alicia
"""

def reverse_seq(n):
    reversed_list = []
    for counter in range(n,0,-1):
        reversed_list.append(counter)
    return reversed_list
print(reverse_seq(8))