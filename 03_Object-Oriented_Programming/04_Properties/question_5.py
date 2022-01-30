##### BankAccount Class Continued #####

# Complete the BankAccount class by adding a private attribute named balance and implementing 
# a getter and setter for it.  For this question, you should use the @property decorator.
# If any of the listed constraints are broken, your method should not update the balance.

# The constraints on the balance attribute are as follows:

##### The balance must always be at least 0.
##### The balance may not exceed 100,000.
##### The balance must be a number.
##### When the balance is retrieved, it is always rounded to the nearest dollar.

# See below for the expected output of a program that uses the BankAccount class.

# >>> account = BankAccount("Tim")
# >>> print(account.balance)
# 0
# >>> account.balance = 17.3
# >>> print(account.balance)
# 17

##### Solution 1 #####
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, balance):
        if type(balance) not in [int, float]:
            return

        if balance < 0 or balance > 100000:
            return

        self._balance = balance

##### Solution 2 #####
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    def get_balance(self):
        return round(self._balance)

    def set_balance(self, balance):
        if type(balance) not in [int, float]:
            return

        if balance < 0 or balance > 100000:
            return

        self._balance = balance

    balance = property(get_balance, set_balance)