class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:",amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:",amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("current_balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Added Interest:", interest)

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrawn with overdraft:", amount)
        else:
            print("Overdraft limit exceeded")

s = SavingsAccount("abc", 2000, 5)

s.deposit(1000)
s.add_interest()
s.withdraw(2000)
s.display_balance()

c = CurrentAccount("Raj", 3000, 2000)
c.deposit(500)
c.withdraw_with_overdraft(4500)
c.display_balance()
