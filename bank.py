#we're going to call out a module we created ourself
from account import Account #This instance, "account" is the name of the file and "Account" isi the name of the class in the account file

class Bank:
    def __init__(self):
        self.accounts = {} #we're using plural (accounts) because bank.py will hamdle multiple accounts

    def create_account(self,name,initial_deposit): #self(the person creating the account), his nanme ,and initial deposit made
        if name not in self.accounts:
            if initial_deposit >= 0:
                self.accounts[name] = Account(name,initial_deposit) #[name] takes the position/index. YOu get the first person's nanme
                print("Account Created Successfully")    
            else:
                print("Initial deposit must not be 0")
        else:
            print("Account with that name already exists")
    
    def deposit(self,name,amount):
        #note name has already been added or created so
        if name in self.accounts:
            self.accounts[name].deposit(amount)
            print("Deposit Successful")
    
    def withdraw(self,name,amount):
        #we're checking if the name is there
        if name in self.accounts:
            if self.accounts[name].withdraw(amount):
                print("Withdrawal Successful")
            else:
                print("Account not found")

    def check_balance(self,name):
        if name in self.accounts:
            balance = self.accounts[name].get_balance() #referencing the function get_balance() created in the module/file account and applying it.
            print(f"Account balance: {balance}")
        else:
            print("Account not found")