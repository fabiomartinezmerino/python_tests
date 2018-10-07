#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:03:10 2018

@author: Alicia
"""



lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

billing = [letter1 + letter2 + number1 + number2 for letter1 in lowercase for letter2 in lowercase
           for number1 in digits for number2 in digits]

print (billing)
