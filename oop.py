class BankAccount:
 def __init__(self,owner_name,starting_balance):
        self.name = owner_name
        self.balance = starting_balance
        print(f"Account created for {self.name} with starting balance ${self.balance}.")


 def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Deposited ${amount}. New balance for {self.name} is  ${self.balance}.")
 
my_account = BankAccount("ikenna",1000)
my_account.deposit(500)
