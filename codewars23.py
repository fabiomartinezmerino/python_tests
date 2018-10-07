#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

#import operator
def min_sum(arr):
    # Your code here
    
    my_list_of_products = []
    my_list_of_products = sorted(arr)
    
    counter = 0
    
    first_array=[]
    second_array=[]
    
    sum_of_products=0
    
    for counter in range(0,len(my_list_of_products),2):
      first_array.append(my_list_of_products[counter])
      
      counter+=1
      
    
    my_list_of_products = sorted(arr,reverse=True)
    
    for counter in range(0,len(my_list_of_products),2):
        second_array.append(my_list_of_products[counter])
        
        counter+=1
      
      
      
      
      
      
     
    
    definite_array = zip (first_array,second_array)
    
    for a,b in definite_array:
        sum_of_products+=a*b    
    
    
    
    
    
    
    
    
    return sum_of_products

    
    
    
    
    
    
    
    
    
    
    
    """
    for pairmultiply in itertools.permutations(arr,len(arr)):
        sumbuf=0
        for i in range(0,len(arr),2):
            sumbuf+=(pairmultiply[i]*pairmultiply[i+1])
        my_list_of_products.append(sumbuf)
    my_list_of_products = set(my_list_of_products)
    

    print(my_list_of_products)
    """

    
    
   

print(min_sum([12,6,10,26,3,24]))