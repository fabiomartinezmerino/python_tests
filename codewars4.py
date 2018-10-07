#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 18:23:39 2018

@author: Alicia
"""

def expression_matter(a, b, c):
   list_of_results=[]
   list_of_results.append(a*b*c)
   list_of_results.append((a+b)*c)
   list_of_results.append(a+b+c)
   list_of_results.append(a*(b+c))
   return max(list_of_results)
    
    
    
    