import re

class ATM:
    def __init__(self, pin, balance=50000):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def validate_pin(self, entered_pin):
        pattern = r"^\d{4}$"  
        if re.match(pattern, entered_pin) and entered_pin == self.pin:
            return True
        return False

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")
        return self.balance

    def mini_statement(self):
        return self.transaction_history[-5:] 
    

obj=ATM(1234)
obj.pin
obj.balance
obj.transaction_history