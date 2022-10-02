
class BankAccount:
    def __init__(self, int_rate, balance= 0): 
        self.int_rate= int_rate
        self.balance= balance

# add a deposit to  the bank account class 
    def deposit(self, amount):
        self.balance += amount
        return self
    # add a withdraw method to  the bank account class 
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")
            self.balance = self.balance - 5
        return self

    # @staticmethod
    # def can_withdraw(self,amount):
    #     if self.balance - amount < 0:
    #         return False
    #     else:
    #         return True
        
        # def display_account_info(self):print to the console: eg. "Balance: $100
    def display_account_info(self):
        print(self.balance)
        return self


    # def yield_interest(self):increases the account balance by the current balance *
    #  the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
            return self

# To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
bankAccount1= BankAccount(.02, 500)
bankAccount1.deposit(200).deposit(9.75).withdraw(50).yield_interest().display_account_info()



lolabank= BankAccount(.03,600)
lolabank.deposit(50).deposit(300).withdraw(75).withdraw(25).withdraw(100).withdraw(50).yield_interest().display_account_info()

jasmine=BankAccount(.02,1000)
jasmine.display_account_info().withdraw(1500).display_account_info()





