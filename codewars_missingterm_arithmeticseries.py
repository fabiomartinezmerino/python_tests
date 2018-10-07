#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 23:08:19 2018

@author: Alicia
"""

def find_missing(sequence):
    """
    input: a ist with an arithmetic series. Minimum 3 terms.
    One missing term neither the first nor the last
    output:missing term
    """
    
    pre_distance = 0
    post_distance = 0
    
    for index in range (0,len(sequence)-2):
        
        """ just iterate over list and compare step size between "thrices" of numbers
            if step size is equal no missing term, but otherwise we have a missing term. 
            All that remains is to ascertain if missing term is btween first and second element or between
            second and third. Abs is to reckon with the fact that step size can be a negative number
        
        """
        
        
        pre_distance = sequence[index+1]-sequence[index]
        post_distance = sequence[index+2]-sequence[index+1]
        
        if pre_distance == post_distance:
            continue
        if abs(pre_distance) > abs(post_distance):
            return sequence[index] + post_distance
        else:
            return sequence[index+1] + pre_distance


print(find_missing([-2,-4,-6,-8,-10,-12,-14,-16,-18,-20,-22,-24,-28]))