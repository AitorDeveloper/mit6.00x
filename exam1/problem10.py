def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    for x in range(n / 24 + 1):
        for m in range(n / 8 + 1):
            for s in range(n / 5 + 1):
                if x * 24 + m * 8 + s * 5 == n:
                    return True
    return False

for pens in range(-100, 100):
    print pens, numPens(pens)
