#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:59:34 2018

@author: Alicia
"""


_loaded  = False

fibcache = {}

def load_fib(my_list):
    global fibcache
    global _loaded
    if not _loaded:
        _loaded = True
        my_index = 0
        for i in my_list:
            fibcache[my_index] = i
            my_index +=1
    return

def fib(n):
    load_fib([1,1])
    if n in fibcache.keys():
        return fibcache[n]
    else:
        fibcache[n] = fib(n-1) + fib(n-2)
        return fibcache[n]
    




print(fib(5))