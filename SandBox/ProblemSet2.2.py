                  
#Test Case 1:
balance = 3329
annualInterestRate = 0.2



minimumFixedPayment = 0.0

myBalance = balance

monthlyInterestRate = annualInterestRate/12.0


while myBalance > 0.0:

    # Increment minimum monthly fixed payment by $10 each time through loop
    minimumFixedPayment += 10.0

    for month in range (0, 12):

        # Apply payment to balance
        myBalance -= minimumFixedPayment

        # Add interest to balance
        myBalance += (myBalance * monthlyInterestRate)

    if myBalance > 0:
        # Reset balance each time through loop
        myBalance = balance


print ("Lowest Payment " + str(minimumFixedPayment))
