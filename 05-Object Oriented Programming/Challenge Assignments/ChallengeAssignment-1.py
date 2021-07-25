# For this challenge, create a bank account class that has two attributes:
# owner , balance
# and two methods:
# deposit , withdraw
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    
    def __init__(self,owner,balance):
    
        self.owner = owner
        self.balance = balance
    
    def deposite(self,deposite):
        self.balance = self.balance + deposite
        return 'Deposite Accepted'

    def withdraw(self,withdrw):
        if withdrw > self.balance:
            print('Funds Unavailable!')
        else:
            self.balance = self.balance - withdrw
            return 'Withdrawal Accepted'

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount balance:{self.balance}'

acc1 = Account('Nel',100)
print(acc1)
print(acc1.deposite(100))
print(acc1)
print(acc1.withdraw(50))
print(acc1)