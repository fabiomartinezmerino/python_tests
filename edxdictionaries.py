#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 23:19:55 2018

@author: Alicia
"""



def how_many(animals):



        animal_counter = 0

        for animals_keys in animals.keys():

    
            animal_counter+=len(animals[animals_keys])
    
        return (animal_counter)

"""animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
"""


print(how_many({'u': [10, 15, 5, 2, 6], 'B': [15]}))


        