#
#  Practical Test 3 
#
#  accounts.py - class for bank accounts
#  
#  Student Name   :
#  Student Number :
#  Date/prac time :
#
class BankAccount ():
    interest_rate = 0.05 #  class variable interest rate
    def __init__(self, name, number, balance):
        self.name = name #  instance variable name
        self.num = number #  instance variable num
        self.bal = balance #  instance variable bal

    def withdraw(self, amount):
        if self.bal < amount:
            raise Exception(str(self.bal), 'Exception: Withdrawal exceeds balance')
        else:
            self.bal = self.bal - amount

    def deposit(self, amount):
        self.bal = self.bal + amount

    def add_interest(self):
        self.bal += self.bal * self.interest_rate
    
    def charge_fee(self):
        self.bal = self.bal - 10
