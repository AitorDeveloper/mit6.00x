def genPrimes():
    primes = []
    x = 2
    while True:
        ifPrime = True
        for prime in primes:
            if x % prime == 0:
                ifPrime = False
        if ifPrime == True:
            primes.append(x)
            yield x
        x += 1
