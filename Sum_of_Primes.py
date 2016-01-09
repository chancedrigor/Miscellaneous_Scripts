

def sumPrimesTo(limit):  # Exclusive
    # Prime Sieve
    p = [True] * limit
    p[0] = p[1] = False

    for (i, isPrime) in enumerate(p):
        if isPrime:
            for n in range(i*i, limit, i):
                p[n] = False
    return sum(x for x in range(2, limit) if p[x])
