# Week 1 Final Project // Banking Application
balance = 10000
while True:
    print()
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Select Option: ")
    
    if choice == "1":
        print("Balance: ", balance)
    
    elif choice == "2":
        amount = int(input("Deposit Amount: "))
        balance = balance + amount
        print("Deposit Successful")
    
    elif choice == "3":
        amount = int(input("Withdraw Amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
        
        if amount > balance:
            print("Insufficient Funds")
    elif choice == "4":
        print("Goodbye")
        break
        
    
    
  
    