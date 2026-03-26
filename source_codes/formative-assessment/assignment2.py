class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate
        self.min_balance = 500  # Minimum threshold

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print(f"Transaction denied. Must maintain ${self.min_balance} minimum.")
        else:
            super().withdraw(amount)

    def apply_monthly_processing(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Overdraft used. New balance: ${self.balance}")
        else:
            print("Overdraft limit exceeded.")

    def apply_monthly_processing(self):
        fee = 15  # Maintenance fee
        self.balance -= fee
        print(f"Maintenance fee of $15 deducted. New balance: ${self.balance}")

# Testing the logic
accounts = [
    SavingsAccount("SA-001", "U Ba", 1000, 5),
    CurrentAccount("CA-002", "Daw Mya", 200, 500)
]

for acc in accounts:
    acc.apply_monthly_processing()