# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:16:55 2016

@author: Cheng
"""

factors = [x for x in range(999, 99, -1)]
products = []
temp = 0

def isPalindrome(pInt):
    pString = [i for i in str(pInt)]
    rejected = False
    for (index, value) in enumerate(pString):
        if value != pString[-(index + 1)]:
            rejected = True
            break
    return not rejected

for (n, i) in enumerate(factors):
    for j in factors[n:]:
        products.append(i*j)

for p in products:
    if isPalindrome(p):
        if p > temp:
            temp = p
print(temp)
