class BankAccount:
  # Constructor method to initialize the bannk account with account number, balance, and owner name
  def __init__(self, account_number, balance, owner_name):
    self.account_number = account_number
    self.balance = balance
    self.owner_name = owner_name
  
  def deposit(self, amount):
    self.balance = self.balance + amount
    print(f"Deposited {amount}. New balance: {self.balance}")

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds.")
      return
    
    self.balance = self.balance - amount
    print(f"Withdrew {amount}. New balance: {self.balance}")

  def check_balance(self):
    print(f"Current balance for {self.owner_name}: {self.balance}")

def main():
  account1 = BankAccount("123456", 1000, "John Doe")
  print(f"Account Number: {account1.account_number}, Owner: {account1.owner_name}, Balance: {account1.balance}")
  account2 = BankAccount("654321", 500, "Jane Smith")
  print(f"Account Number: {account2.account_number}, Owner: {account2.owner_name}, Balance: {account2.balance}")
  account1.deposit(500)
  account1.withdraw(200)
  account1.withdraw(1500)
  account1.check_balance()
  account2.check_balance()

# DUNDER Methods (Double Underscore Methods) are special methods in Python that have double underscores before and after their names. They are also known as "magic methods" or "special methods". These methods allow you to define how your objects behave with built-in operations, such as addition, string representation, and more.
if __name__ == "__main__":
  main()
  