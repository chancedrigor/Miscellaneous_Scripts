# not a sieve of eratosthenes
# prime generator

START = 1  # First number looked at
END = floor(sqrt(600851475143))  # Last number looked at

PRIMES = [2]

for i in range(START, END, 1):
    for p in PRIMES:
        if i % p == 0:
#            print(i , "is a product of" , p , "and" , int(i/p))
            break
        elif p == PRIMES[-1] and i != 1:
            PRIMES.append(i)

print(PRIMES)
print("A total of", len(PRIMES), "primes between", START, "and", END)
