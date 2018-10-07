#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 21:44:39 2018

@author: Alicia
"""

def adjacent_element_product(array):
    """
    input: array is a list whose elements are to be taken in pairs, sequentially, to
    be multiplied and stored in another list, product_list

    return: max_product is the greatest of all the former mentioned products

    """

    return max(item[0]*item[1] for item in zip(array,array[1:]))

print(adjacent_element_product([3, 6, -2, -5, 7, 3]))