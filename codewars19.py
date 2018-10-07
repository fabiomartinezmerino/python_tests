#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:36:28 2018

@author: Alicia
"""

import itertools

def find_min_max_product(arr, k):
    """
    input: arr list containing a sequence of numbers positive and negative
    input: k represent how many factors we have to multiply in order to obtain\
    maximum and minimum product of k factors of the list arr
    return: minimum and maximum values

    """
    
    if (len(arr)<k):
        return None
    
    # in this list we store the k-tuples of arr numbers
    my_permutation_list = itertools.combinations(arr,k)


    counter = 0
    product_list = []

    
    #Now we do the product of the k-tuples and store them in product_list
    for i in my_permutation_list:
        print ("Permutación numero %d:" % (counter))
        counter+=1
        product = 1
        for number in i:
            product *= number
        
        product_list.append(product)
        print ("El producto es %d:" % product)
    
    print(product_list)
    
    #Now we look for min and max value and store them in the list we will
    #return
    
    result_list = []
    
    result_list.append(min(product_list))
    result_list.append(max(product_list))
    
    result_list = tuple(result_list)
    return result_list
    
print (find_min_max_product([3,-1,-2,4,5,3,7],4))