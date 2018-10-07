#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:43:14 2018

@author: Alicia
"""


def max_number(n):
    intermediate_list = [number for number in str(n)]    
    intermediate_list.sort(reverse=True)
    return int("".join(str(character) for character in intermediate_list))
print (max_number(1214598))