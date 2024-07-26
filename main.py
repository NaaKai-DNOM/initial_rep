from bank import Bank
#We need to write code to run the application. We will call it from the bank

def main():
    bank = Bank()

    #This will execute only when the condition is true
    while True:
        print("\nWelcome to D Bank\n")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        #We're going to store all these options in a variable called choice
        choice = input("Enter your preferred choice: ")
    
        #We want to write functionalities for all the five choices we have
        if choice == "1":
            name = input("Enter your name: ") #nb: if you used id, you use id. If it was randomly selected during creation, you'll realizes changes.
            initial_deposit = float(input("Enter initial_deposit amount: "))
            bank.create_account(name,initial_deposit) #calling the bank file and the respective class. name and initial_deposit are the arguments to be passed which were the parameters created when function was created.

        elif choice =="2":
            name = input("Enter your account name: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(name,amount)

        elif choice == "3":
            name = input("Enter your account name: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(name,amount)

        elif choice == "4":
            name = input("Enter your account name: ")
            bank.check_balance(name)

        elif choice == "5":
            print("Thank you for Banking with us!")
            break

        else: 
            print("Invalid choice entered. Please try again.")
        
if __name__ == main():
    main()