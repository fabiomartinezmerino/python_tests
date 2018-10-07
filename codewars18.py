#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 18:17:06 2018

@author: Alicia
"""

def nb_dig(n, d):
    """
    n is a number >=0 we are going to take all squares up to n*n
    d is an integer 0<=d<=9 and we are going to sum up how many times d\
    appears in all that numbers
    return number_of_times_d_appears that is how many times d appears in all\
    the squares
    """
    # List where squares will be stored
    
    list_of_squares = []
    
    # We compute the squares and stored them in the list
    
    for square_operation_step in range(0,n+1,1):
        
        list_of_squares.append(square_operation_step**2)
        
    print(list_of_squares)
    
    # Now we are going to count how many times d appears, we will stored \
    # results in partial_number_of_d
    partial_number_of_d = 0
    
    for number in list_of_squares:
        
        #print("The number %d appears in %d %d times" % \
        #     (d,number,int(str(number).count(str(d)))))
        
        partial_number_of_d += int(str(number).count(str(d)))
    
    return partial_number_of_d

print (nb_dig(5750, 0))

