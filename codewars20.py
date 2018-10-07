#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 18:38:53 2018

@author: Alicia
"""

def sentence(List):
    """
    input List is a list of dictionaries whose values are going to be sorted by
    key
    return result_string is a string comprised by values of List sorted
    
    """
    
    # we obtain a sorted list of input array of dictionaries (List) ' s values
    
    # we create a dictionary from list of dictionaries
    
    myDict = dict()
    
    # we iterate on list of dictionaries obtain each dictionary and add it as
    # a new entry of a bigger dictionary
    
    for v in List:
        myDict.update(v)

    # print output for debugging purposes
    print (myDict)

    
    list_of_sorted_keys = sorted(myDict.keys(),key=int)
    # print output for debugging purposes
    print (list_of_sorted_keys)
    
    # this string will contained returned value
    result_string = ""
    
    # with sorted list of keys we iterate on dictionary and obtain values to
    # build up returned string
    
    for key_string in list_of_sorted_keys:
        result_string = result_string + (myDict.get(key_string)) + " "
    
    # print output for debugging purposes
    print (result_string)
    
    
    return result_string.rstrip()


print(sentence([
        {'4': 'dog' }, {'2': 'took'}, {'3': 'his'}, 
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'} 
       ]))
    
    
