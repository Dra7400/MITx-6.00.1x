# Paste your code into this box
monthlyInterestRate = annualInterestRate/12.0
fixedPayment = 10
def calculate(balance,monthlyInterestRate):
    i = 1
    while i <= 12:
        unpaidBalance = balance - fixedPayment
        balance = unpaidBalance + unpaidBalance * monthlyInterestRate
        i += 1
    return balance
while calculate(balance,monthlyInterestRate) > 0:
    fixedPayment += 10
    calculate(balance,monthlyInterestRate)
print("Lowest Payment is:" + " " + str(fixedPayment))
