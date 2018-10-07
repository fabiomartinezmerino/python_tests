#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:26:43 2018

@author: Alicia
"""

_loaded  = False

tribcache = {}

def load_trib(my_list):
    global tribcache
    global _loaded
    if not _loaded:
        _loaded = True
        my_index = 0
        for i in my_list:
            tribcache[my_index] = i
            my_index +=1
    return

def trib(signature,n):
    global tribcache
    global _loaded    
     
    
    load_trib(signature)
    if n in tribcache.keys():
        return tribcache[n]
    else:
        tribcache[n] = trib(signature,n-1) + trib(signature,n-2)+trib(signature,n-3)
        return tribcache[n]
    

def tribonacci(signature,n):
    global tribcache
    global _loaded      
    
    
    my_list = list(trib(signature,i) for i in range(0,n))

    tribcache = {}
    _loaded = False

    return my_list

    
    
    
    #return trib(signature,n-1)


print(tribonacci([0,1,1],10))