# Paste your code into this box
i = 1

while i <= 12:
    monthlyInterestRate = annualInterestRate/12.0
    minimumMonthlyPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumMonthlyPayment
    updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
    balance = updatedBalance
    i += 1
print("The Remaining Balance is:" + " " + str(round(balance,2)))

