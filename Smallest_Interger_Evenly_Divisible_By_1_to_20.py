# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 23:21:54 2016

@author: Cheng
"""

from math import factorial

numbers = range(20, factorial(20) + 20, 20)

for i in numbers:
    for j in range(2, 21):
        if i % j is not 0:
            foundFlag = False
            break
        else:
            foundFlag = True
    if foundFlag:
        print(i)
        break
