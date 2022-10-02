from bankaccount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print (self.account.balance)

# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print (self.account.balance)
# Add a display_user_balance method to the User class that displays user's account balance

    def display_user_balance(self):
        self.account.display_account_info()
        print (self.account.display_account_info)

bankAccount1= BankAccount(.02, 500)
bankAccount1.deposit(200).deposit(9.75).withdraw(50).yield_interest().display_account_info()



lolabank= BankAccount(.03,600)
lolabank.deposit(50).deposit(300).withdraw(75).withdraw(25).withdraw(100).withdraw(50).yield_interest().display_account_info()

jasmine=BankAccount(.02,1000)
jasmine.display_account_info().withdraw(1500).display_account_info()

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.