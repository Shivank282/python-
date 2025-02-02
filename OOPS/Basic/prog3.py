class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}, New Balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: {amount}, Remaining Balance: {self.balance}"
        return "Insufficient balance!"

# Example Usage
account = BankAccount(500)
print(account.deposit(200))  # Output: Deposited: 200, New Balance: 700
print(account.withdraw(100)) # Output: Withdrew: 100, Remaining Balance: 600
