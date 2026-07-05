class BankAccount:
  def __init__(self, pin):
    self.account_balance = 0
    self.pin = pin
  def deposit(self, pin, amount):
    if pin == self.pin:
      self.account_balance += amount
      return self.account_balance
    else:
      return "Invalid PIN."
  def withdraw(self, pin, amount):
    if pin == self.pin:
      if amount <= self.account_balance:
        self.account_balance -= amount
        return f"{amount} withdrawn."
      else:
        return "Insufficient Funds"
    else:
      return "Invalid PIN."
  def get_balance(self, pin):
    if pin == self.pin:
      return self.account_balance
    else:
      return "Invalid PIN."
  def change_pin(self, old_pin, new_pin):
    if old_pin == self.pin:
      self.pin = new_pin
      return "PIN succesfully changed."
    else:
      return "Invalid PIN."

class SavingsAccount(BankAccount):
   def __init__(self, pin, interest_rate):
      super().__init__(pin)
      self.interest_rate = interest_rate
   def apply_interest(self):
      self.account_balance += self.interest_rate * self.account_balance
      
class FeeSavingsAccount(SavingsAccount):
   def __init__(self, pin, interest_rate, fee):
      super().__init__(pin, interest_rate)
      self.fee = fee
   def withdraw(self, pin, amount):
      if pin == self.pin:
        if amount + self.fee <= self.account_balance:
             self.account_balance -= self.fee
             return super().withdraw(pin, amount)
        else:
             return "Insufficient Funds"
      else:
         return "Invalid PIN."
