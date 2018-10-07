#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:09:48 2018

@author: Alicia
"""

def isPrime(n):
    return all(n%j for j in range(2, int(n**0.5)+1)) and n>1

def minimunNumber(inputListOfNumbers):

    
    numberToTest = sum(inputListOfNumbers)
    theNumber = numberToTest
    while True:
        theNumber+=1
        if(isPrime(theNumber)):
            break

    print("Next Prime Number = " + str(theNumber))
    print("NUmero a añadir a la lista = " + str(theNumber-numberToTest))

    return theNumber-numberToTest



print(minimunNumber([2,12,8,4,6,1800]))


