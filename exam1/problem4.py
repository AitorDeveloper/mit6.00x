secret = 100

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
    It takes as a parameter one number and returns:
    *  -1 if the number is less than the secret number
    *  0 if the number is equal to the secret number
    *  1 if the number is greater than the secret number
                        
    returns: integer, the secret number
    ''' 
    guess = 1
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            guess += 1
        elif sign == 1:
            guess -= 1
        else:
            foundNumber = True
    return guess

def isMyNumber(x, number = secret):
    print x, number
    if x > number:
        return 1
    elif x < number:
        return -1
    else:
        return 0

jumpAndBackpedal(isMyNumber)
