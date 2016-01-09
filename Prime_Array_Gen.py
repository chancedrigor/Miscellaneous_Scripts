# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:42:36 2016

@author: Cheng
"""

Primes = [2]
i = 1

while len(Primes) < 10001:
    for p in Primes:
        if i % p == 0:
            break
        elif p == Primes[-1] and i != 1:
            Primes.append(i)
    i += 1

print(Primes[-1])
