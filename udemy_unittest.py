#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:50:01 2018

@author: Alicia
"""




import unittest

def fun(x):
    return x + 1



class MyTest(unittest.TestCase):
    def test(self):
           self.assertEqual(fun(3), 4)
           
           
           
           
if __name__ == '__main__':
    unittest.main()


    
