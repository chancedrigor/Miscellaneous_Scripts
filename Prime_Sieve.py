# Sieve of Eratosthenes

from math import *


def prime_sieve(limit):
    p = [True] * limit
    p[0] = p[1] = False

    for (i, isPrime) in enumerate(p):
        if isPrime is True:
            for j in range(i*i, limit, i):
                p[j] = False
    return p

p1 = prime_sieve(floor(sqrt(600851475143)))
plarge = 0

for (i, isPrime) in enumerate(p1):
    if isPrime and 600851475143 % i == 0:
        plarge = i

print(plarge)