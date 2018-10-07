#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:35:48 2018

@author: Alicia
"""

def duplicate_count(text):
    # Your code goes here
    """
    input: string to asses
    output: number of characters with duplicates
    
    Count the number of Duplicates
    Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

    Example
    "abcde" -> 0 # no characters repeats more than once
    "aabbcde" -> 2 # 'a' and 'b'
    "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
    "indivisibility" -> 1 # 'i' occurs six times
    "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
    "aA11" -> 2 # 'a' and '1'
    "ABBA" -> 2 # 'A' and 'B' each occur twice
    """

    #we "lowercase" the text so no confusion arises
    
    transformedtext = text.lower()
    
    #we get a set with unique values
    
    buffer_set = set (transformedtext)
    
    #then we remove this unique values from original list - text. Remainning characters will be
    #duplicate ones
    
    #we use a list to be able pop unique values. Only duplicated will remain
    
    buffer_list = list(transformedtext)
    
    for item in buffer_set:
        buffer_list.remove(item)
    
    #now we build up again buffer_set with buffer_list to eliminate duplicates. Remaining characters
    #are the ones originally repeating so only remain to count items
    
    buffer_set = set (buffer_list)
    
    return len(buffer_set)


print(duplicate_count("aaaaaabbbbbbbbccccccCCCCCddeefghijklllll"))

        