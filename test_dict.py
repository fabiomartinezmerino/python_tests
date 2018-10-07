#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:12:17 2018

@author: Alicia
"""

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
animals['a']
print(animals)
print('baboon' in animals.values())
del(animals["b"])
print(len(animals))