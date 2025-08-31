balance=0
while True:
    option1="Deposit"
    option2="Withdraw"
    option3="Exit"
    print((option1,option2,option3))
    userInput=input("Choose anyone from the available option: ")
    if userInput==option1:
        print("Current balance is: ", balance)
        amount=int(input("Enter the amount to deposit: "))
        balance+=amount
        print("Updated balance is : ", balance)
    elif userInput==option2:
        print("Current balance is: ", balance)
        amount=int(input("Enter the amount to withdraw: "))
        if amount>balance:
            print("Insufficient balance!!")
        else:
            balance-=amount
            print("Updated balance is : ", balance)
    elif userInput == option3:
        print("Exited successfully")
        break
    else:
        print("Invalid input")
