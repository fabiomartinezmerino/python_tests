#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:45:42 2018

@author: Alicia
"""
def biggest(aDict):
    """
    aDict: dictionary containing lists to iterate over
    returns: key corresponding to longest list
    """
    winner_key = ""
    winner_len = 0
    for my_key in aDict.keys():
        if len(aDict[my_key]) > winner_len:
            winner_len = len(aDict[my_key])
            winner_key = my_key
    return winner_key
    
    
    
    
    
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))