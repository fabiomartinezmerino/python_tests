#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:22:05 2018

@author: Alicia


You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.

"""

import re

pswd ="2wfAyyy1"



#regex=r"(^.(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[\_\-\\\^\&\.\$\|\?\*\+\(\)\[\{\] :;,=!#}@<>\"_]).{6,})"

if re.match(r"^\w*(?=.{6,})(?=\w*[a-z])(?=\w*[A-Z])(?=\w*\d)\w*$",pswd):
    print ("Match")
else:
    print ("Not Match")

 # ^.*
 # .*$