#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:31:22 2018

@author: Alicia
"""

def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

#print(times_tables())


print(times_tables() == [producti * productj for producti in range(10) for productj in range(10)])


