print "Please think of a number between 0 and 100!"

guess = 50
start = 0
end = 100

while True:
    print "Is your secret number " + str(guess) + "?"
    resp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if resp not in ['l', 'h', 'c']:
        print "Sorry, I did not understand your input."
    elif resp == 'l':
        start = guess
        guess = start + (end - start) / 2
    elif resp == 'h':
        end = guess
        guess = start + (end - start) / 2
    else:
        break

print 'Game over. Your secret number was: ' + str(guess)



    


