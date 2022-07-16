#
#  Practical Test 3 
#
#  testAccounts.py - program to test functions of accounts.py
#  
#  Student Name   :
#  Student Number :
#  Date/prac time :
#
from accounts import BankAccount

def balances():
    print('\n#### Balances of All Accounts####\n')
    total = 0
    for i in range(len(my_accounts)):
        print("Name: ", my_accounts[i].name, "\tNumber: ", my_accounts[i].num, \
              "\tBalance: ", my_accounts[i].bal)
        total = total + my_accounts[i].bal
    print("\t\t\t\t\tTotal: ", total)

print('\n#### Bank Accounts ####\n')
my_accounts = []

# add code for tasks here
sav = BankAccount('Savings', '500000-1', 5000)
evr = BankAccount('Everyday', '500000-2', 500)

my_accounts.append(sav)
my_accounts.append(evr)

sav.deposit(500)
try:
    my_accounts[1].withdraw(50)
    my_accounts[1].withdraw(5000)
except Exception as err:
    print(err)

sav.add_interest()
evr.add_interest()
evr.charge_fee()
sav.charge_fee()

balances()
