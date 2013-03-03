def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    total = 0
    while start < stop:
        total += f(start) * step
        start += step
    return total
