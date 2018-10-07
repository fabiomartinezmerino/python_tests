#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:34:29 2018

@author: Alicia
"""

def reverse_words(text):
  #go for it
  intermediate_list = text.split(" ")
  returned_string = ""
  for word in intermediate_list:
      returned_string += (reverse_word(word)+" ")
  return returned_string.rstrip()
def reverse_word(word):
    return word[::-1]


print(reverse_words("Hola mundo"))