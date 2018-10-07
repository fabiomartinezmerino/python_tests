#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:07:35 2018

@author: Alicia
"""

def max_number(n):
#    intermediate_list = [number for number in str(n)]    
#    intermediate_list.sort(reverse=True)
    return int("".join(str(character) \
                       for character in sorted([number for number in str(n)],\
                                                reverse=True)))
print (max_number(1214598))