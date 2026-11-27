class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
        
    def deposit(self,amount):
        self.balance +=amount
        print("Money Deposite Successfully!")
        
    def withdraw(self,amount):
        if self.balance < amount:
            print("No sufficient Balance ")
        else:
            self.balance -=amount
            print("Money Withdraw Successfully!")
        
    def show_balance(self):
        print("Current Balance:",self.balance)
        
class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance,interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate=interest_rate
        
    def add_interest(self):
        interest = (self.balance * self.interest_rate)/100
        self.balance +=interest
        print("Balance After Interest:",self.balance)

account1 = SavingAccount("Aakash", 10000, 5)

account1.show_balance()
account1.add_interest()
account1.show_balance()