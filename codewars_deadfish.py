#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:51:43 2018

@author: Alicia
"""

"""
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

input: a string which yo have to parse, each character is a command
output: a list with so many items as output commands you have come across

"""
import numpy as np
def parse(data):
    """
    input: a string which yo have to parse, each character is a command
    output: a list with so many items as output commands you have come across    
    """
    result_list = []
    initial_data = 0
    for character in data:
        if character == "i":
            #print("i")
            initial_data+=1
        elif character == "d":
            #print("d")
            initial_data-=1
        elif character == "o":
            #print ("o")
            result_list.append(initial_data)
        elif character == "s":
            #print("s")
            #initial_data=np.square(initial_data)
            initial_data = pow(initial_data,2)
        else:
            pass
    return result_list
            
    
print("String to test: {0} \nResult:{1}".format("isoisoiso",parse("isoisoiso")))
