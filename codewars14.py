#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:45:10 2018

@author: Alicia
"""

def test(r):
    #r contains a list with alumni's grades
    average_results = round(sum(r)/len(r),3)
    number_of_h = r.count(10) + r.count(9)
    number_of_a = r.count(8) + r.count(7)
    number_of_l = r.count(6) + r.count(5) + r.count(4)+ r.count(3)\
    + r.count(2) + r.count(1) + r.count(0)
    if number_of_a + number_of_l:
        return [average_results, {"h":number_of_h,"a":number_of_a,\
                                  "l":number_of_l}]
    else:
         return [average_results, {"h":number_of_h,"a":number_of_a,\
                                  "l":number_of_l}, "They did well"]

print (test([10,8,9,0,0,0,1,2,7,7]))
#print test([10,9,9,8,8,8,7,6,4,2,3,4,0,1])