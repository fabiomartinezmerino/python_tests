#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:20:21 2018

@author: Alicia
"""

def remove_min_from_list(mylist):
    if mylist:
        mylist.remove(min(mylist))
    return mylist

print(remove_min_from_list([2,1,34,23,2]))


    