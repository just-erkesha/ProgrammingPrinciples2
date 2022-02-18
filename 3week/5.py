class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def deposit(self, put):
        self.put=put
        self.balance+=put

    def withdraw(self, take):
        self.take=take
        if take<=self.balance:
            self.balance-=take
            print(f'Your current balance: {self.balance}')
        else: 
            print(f'You cannot withdraw! Current balance: {self.balance}')

Process = Account(input(), int(input()))
Process.deposit(int(input("Put money")))
Process.withdraw(int(input("Take money")))
Process.deposit(int(input("Put money")))
Process.withdraw(int(input("Take money")))