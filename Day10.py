class Deposit():
    def __init__(self,amount):
        amount = float(input("Enter amount to be deposit:"))
        self.amount = amount
        self.balance = self.balance + self.amount
        print("\n Amount deposited:",self.amount , "Rupees")
        print("Net Available Balance=", self.balance,"Rupees")
class Withdraw():
    def __init__(self,money):
        money = float(input("Enter amount to be Withdrawn:"))
        self.money = money
        self.balance = self.balance - self.money
        if (self.balance>=self.money):
            print("\n You Withdraw:",self.money,"Rupees")
            print("Net Available Balance=", self.balance,"Rupees")
        else:
            print("Sorry! Insufficient balance.")
class Bank_Account(Deposit,Withdraw):
    def __init__(self,balance = 0.0):
        self.balance = balance
        Deposit.__init__(self,0)
        Withdraw.__init__(self,0)


ob = Bank_Account()


