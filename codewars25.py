#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 21:27:14 2018

@author: Alicia
"""

def adjacent_element_product(array):
    """
    input: array is a list whose elements are to be taken in pairs, sequentially, to
    be multiplied and stored in another list, product_list

    return: max_product is the greatest of all the former mentioned products

    """

    max_product = []

    for index in range(0,len(array)-1):
        max_product.append(array[index]*array[index+1])

    max_product = sorted(max_product, reverse=True)

    return max_product[0]

print(adjacent_element_product([3, 6, -2, -5, 7, 3]))