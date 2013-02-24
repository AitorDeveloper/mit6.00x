balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalpayed = 0

for month in range(1, 13):
    minterest = annualInterestRate / 12.0
    minpay = monthlyPaymentRate * balance
    totalpayed += minpay
    balance = (balance - minpay) * (1 + minterest)
    print 'Month:', month
    print 'Minimum monthly payment:', round(minpay, 2)
    print 'Remaining balance:', round(balance, 2)

print 'Total payed:', round(totalpayed, 2)
print 'Remaining balance:', round(balance, 2)
