class BankAccount ():
    interest_rate = 0.03
    
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
 
    def deposit(self, amount):
        self.balance = self.balance + amount
 
    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def balances(accounts):
        total = 0
        for i in range(len(accounts)):
            print("Name:", accounts[i].name, "\tNumber: ", accounts[i].number,
                "\tBalance: ", accounts[i].balance)
            total = total + accounts[i].balance
        print("\t\t\t\t\tTotal: ", total)
