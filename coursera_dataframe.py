#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:22:44 2018

@author: Alicia
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
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 2', 'Store 2'])

#print(df.head())

print(df["Item Purchased"])

"""
sd = []
for my_index, my_series in df.iterrows():
    sd.append(my_series.loc["Item Purchased"])
    
print (sd)
"""

df["Cost"]*=0.8

print(df["Cost"])
