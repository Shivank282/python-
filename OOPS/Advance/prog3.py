class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount."

    def check_balance(self):
        return f"Current balance: {self.balance}"

# Example Usage
atm = ATM(1000)
print(atm.deposit(500))   # Output: Deposited 500. New balance: 1500
print(atm.withdraw(700))  # Output: Withdrew 700. New balance: 800
print(atm.check_balance()) # Output: Current balance: 800
