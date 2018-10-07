#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:31:32 2018

@author: Alicia
"""

"""
Pandas Dataframe usage
"""

import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

print(df.head())

#print items or registers indexed as "Store 2"

print(df.loc["Store 2"])

#print values of "Name" of all registers or rows

print(df["Cost"])

#print field Name of items indexed as "Store 1"

print(df.loc["Store 1"]["Name"])

#print fields Name and cost of items indexed as "Store 1" and "Store 2"

print(df.loc[:,["Name","Cost"]])
