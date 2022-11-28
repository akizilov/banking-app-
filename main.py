num_transactions = 0
balance = 0
transaction = "y"

balance = int(input("What is your initial balance? "))


while transaction == "y":
    deposit_or_withdrawal = input("Would you like to make a deposit(d) or withdrawal(w)?")
    if deposit_or_withdrawal == "w":
        amount = int(input("How much would you like to withdraw? "))
        if amount > balance:
            print("You cannot withdraw more than your balance of "+str(balance))
        else:
            balance = balance - amount
    elif deposit_or_withdrawal == "d":
        amount = int(input("How much would you like to deposit? "))
        balance = balance + amount
    elif deposit_or_withdrawal != "d" or "w":
        print("Invalid Entry")
    
    num_transactions += 1
    
    transaction = input("Would you like another transaction(y/n)?  ")

    
#Final output statement to user after user doesn't want to make any more transactions
if num_transactions > 1:
    print("You made "+str(num_transactions)+ " transactions and your final balance is $" + str(balance) + ".")
else:
    print("You made "+str(num_transactions)+ " transaction and your final balance is $" + str(balance) + ".")
