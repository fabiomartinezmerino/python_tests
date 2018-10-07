#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:54:51 2018

@author: Alicia
"""

def unique_in_order(iterable):
    """
    input: list of characters to asses
    output: list with no two repeated characters one beside the other
    
    Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

    For example:

    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1,2,2,3,3])       == [1,2,3]
    
    
    
    """
    iterable=list(iterable)
    returned_list = iterable[0:1]
    
    #buffer_item = ""
    
    for index in range (1,len(iterable)):
        if iterable[index] != iterable [index - 1]:
            returned_list.append(iterable[index])
    
    return returned_list


print(unique_in_order(['A',"A",'B','C',"C",'D','A',"B","B","b",'B']) )      