def isPrime(n):
    if type(n) != int:
        raise TypeError()
    elif n <= 0:
        raise ValueError

    if n % 2 == 0:
        return False

    for i in range(2, n / 2):
        if n % i == 0:
            return False
    
    return True
