#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:08:30 2018

@author: Alicia
"""

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]
    """
    person: a string of a scintist that you haveto split into title and last name and discard
    name
    returns: title and last name
    """


"""
now you have to do the same using lambdas


"""

#option 1
for person in people:
    print(split_title_and_name(person) ==
          (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))
 
#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' 
                + person.split()[-1], people))
