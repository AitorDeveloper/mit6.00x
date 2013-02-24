balance = 999999
annualInterestRate = 0.18

low = balance / 12
hi = (balance * (1 + annualInterestRate / 12.0)**12) / 12.0
monthlyInterest = annualInterestRate / 12

while True:
    fbalance = balance
    monthlyPayment = (low + hi) / 2

    for month in range(1, 13):
        fbalance = (fbalance - monthlyPayment) * (1 + monthlyInterest)

    if fbalance < 0:
        hi = monthlyPayment
    else:
        low = monthlyPayment

    if fbalance < 0 and fbalance > -0.01:
        break

print 'Lowest payment:', round(monthlyPayment, 2)
