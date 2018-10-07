#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 15:29:33 2018

@author: Alicia
"""

import itertools
#import operator
def min_sum(arr):
    #in the following array pairs of number to be multiplied are stored
    arr_of_pairs = []
    #in the following array sums of l/2 summands are stored. Minimum will be\
    #selected
    arr_of_sums = []
    #generate the potential list of pairs to multiply
    for pairs in itertools.combinations(arr,2):
        arr_of_pairs.append(pairs)
    #now we select groups of len/2 pairs with no repeated members and store\
    #to operate with them later on
    counter_of_groups = 0 #when reaches len/2 then the group is ready to be\
    #array to store group of three pairs so we can ensure no repetaed elements
    group_of_thrice = [] 
    
    #for debugging purposes
    print (arr_of_pairs)
    
    for pair_to_mult in arr_of_pairs:
        #we initialize group_of_thrice array
        group_of_thrice.append(pair_to_mult)#this array of thrices already\
        #has an item... len/2 -1 remain to be stored        

        print("Se empieza con el grupo: " + str(group_of_thrice))
        #this while loop is responsible por selecting proper groups of\
        #len/2 pairs
        
        while counter_of_groups < (int(len(arr)/2)):
        
        #this is somewhat inefficient as we always start from the beginning
                    
            for pair_to_mult2 in arr_of_pairs:
                print("Siguiente pareja: " + str(pair_to_mult2))
                #we have to test wether pair_to_mult2 has a repeated item
                add_pair = True
                for number in pair_to_mult2:
                    for item_to_check in group_of_thrice:
                        if(number in item_to_check):
                            add_pair = False
                            print("La pareja: "+str(pair_to_mult2)+" no vale")
                        
                if add_pair:
                    print("La pareja: "+str(pair_to_mult2)+" vale")
                    group_of_thrice.append(pair_to_mult2)
                    print("Dentro de la construccion del grupo: " + str(\
                              group_of_thrice))
                    counter_of_groups+=1
                    break
    
                    
                
        #we already have a valid thrice of pairs, multiply each pair, sum and
        #store
        buffer_to_sum = 0
        
        for items_to_mult in group_of_thrice:
            buffer_to_sum+=items_to_mult[0]*items_to_mult[1]
        
        arr_of_sums.append(buffer_to_sum)
        
        print("Estamos en: " + str(group_of_thrice) + " resultado: " + \
              str(buffer_to_sum))
        #we clean group of thrice
        group_of_thrice = []
        
    
    arr_of_sums = set(arr_of_sums)
    return min(arr_of_sums)

print(min_sum([5,4,2,3]))