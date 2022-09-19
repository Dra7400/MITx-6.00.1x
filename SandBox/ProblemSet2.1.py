# Paste your code into this box



totalPaid = 0.0
monthlyInterestRate = (annualInterestRate/12.0)


count = 1
while count <= 12:
    minMonthlyPayment = monthlyPaymentRate * balance

    balance -= minMonthlyPayment

    balance += (monthlyInterestRate * balance)

    totalPaid += minMonthlyPayment

    count += 1


print ("Remaining balance: " + str(round(balance, 2)))
