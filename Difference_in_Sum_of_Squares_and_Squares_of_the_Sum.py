# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:34:42 2016

@author: Cheng
"""

numbers = range(1, 101)
a = b = 0

for n in numbers:
    a += n*n
    b += n

print(b*b - a)
