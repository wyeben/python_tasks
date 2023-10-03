import random


class Account:
    def __init__(self, account_number, pin):
        self.last_name = None
        self.first_name = None
        self.account_number = account_number
        self.balance = 0.0
        self.pin = pin

    @staticmethod
    def generate_account_number():
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount, pin):
        if self.pin == pin and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_account_number(self):
        return self.account_number

    def register(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_account_number(self, accountNumber):
        self.account_number = accountNumber

    def get_account_details(self):
        return f"{self.first_name} {self.last_name} - {self.account_number}"
