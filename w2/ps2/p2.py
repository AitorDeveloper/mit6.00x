balance = 3926
annualInterestRate = 0.2

monthlyPayment = 0
fbalance = balance

while fbalance > 0:
    fbalance = balance
    monthlyPayment += 10
    totalPayed = 0

    for month in range(1, 13):
        fbalance = (fbalance - monthlyPayment) * (1 + annualInterestRate / 12)
        #print month, fbalance

print 'Lowest payment:', monthlyPayment
