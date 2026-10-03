# deposit, withdraw, balance check and so on

class Bank: 
    def __init__(self,balance):
        self.balance = balance 

    def deposite(self,amount): 
        self.balance += amount

    def withdraw(self,amount): 
        self.balance -= amount

    def get_balance(self): 
        print(f"your current balance is {self.balance}")

ucb = Bank(1000)
ucb.deposite(1000)
ucb.get_balance()










