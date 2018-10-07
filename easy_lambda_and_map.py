#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:59:33 2018

@author: Alicia
"""
my_ = lambda x:3+x
print(list(map(lambda x:3+x,   [3,4,5,6])))
print(list(map(my_,[3,4,5,6,7])))
