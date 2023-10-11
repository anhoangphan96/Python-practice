#For this challenge, create a bank account class that has two attributes:

#owner
#balance
#and two methods:

#deposit
#withdraw
#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn

class BankAccount():
  def __init__(self,owner,balance):
    self.owner = owner 
    self.balance = balance
  def deposit(self,amount):
    self.balance += amount
    print(f"Deposit {amount} successfully! {self.owner}' balance now is {self.balance}")
  def withdraw(self,amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"With draw {amount} successfully! {self.owner}' balance now is {self.balance}")
    else:
      print(f"Funds Unavailable! {self.owner}' balance is {self.balance}")

mark_account = BankAccount("Mark", 5000)
mark_account.deposit(500)
mark_account.withdraw(4000)
mark_account.withdraw(20000)