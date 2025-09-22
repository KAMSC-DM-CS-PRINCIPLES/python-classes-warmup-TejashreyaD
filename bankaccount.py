# TODO create class BankAccount
class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,money):
        if (money>=0):
            self.balance+=money
            return self.balance
    def withdraw(self,money):
        if (money>=0):
            if (money<=self.balance):
                self.balance-=money
                return self.balance
            else:
                return "Insufficient Funds"
    def get_balance(self):
        return self.balance

