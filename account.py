#We're going to create a class that is "class Account". We will include attributes , call a function inside the account
#Since we're starting a bank application we're using the built-in function __init__ (the initializer), deposit, withdrawal, check balance
class Account:
    def __init__(self,name,balance=0):
        #handling account creation
        self.name = name 
        self.balance = balance
    
    def deposit(self,amount):
        #we take the initial balance and add the deposit amount to it
        self.balance += amount

    def withdraw(self,amount):
        #you check the person's name and amount that is to be wihtdrawn. There's a condition because you cant withdraw till zero balance
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient Balance")
            return False
    
    def get_balance(self):
        return self.balance
