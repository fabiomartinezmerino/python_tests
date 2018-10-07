#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 23:22:59 2018

@author: Alicia
"""

def sort_array(source_array):
    """
    Source array is array within wich odd numbers are to be sorted
    return odd_sorted array, even numbers at their places 0 should not
    be moved
    """
    # extract odd numbers and sort them
    # in this list we will store odd numbers
    odd_list=[]
    # in this list we will store the indexes where odd numbers were seated
    indexes_list=[]
    # this integre will keep track of odd number indexes
    index_of_odd = 0
    for number in source_array:
        if number%2 != 0:
            
            odd_list.append(number)
            indexes_list.append(index_of_odd)
        index_of_odd+=1
    #we will print list of odd numbers and their positions
    print(odd_list)
    print(indexes_list)

    #we will sort the list of odd numbers    
    odd_list.sort()
    
    #finally we iterate on the list of odd numbers, already sorted, and keep
    #inserting them into former odd numbers positions
    index=0
    for odd_number in odd_list:
         source_array[indexes_list[index]]=odd_number
         index+=1
    return source_array

print(sort_array([0,3,2,4,7,5]))