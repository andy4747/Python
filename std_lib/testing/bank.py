class LowBalanceError(Exception):
	def __init__(self,message):
		self.message=message

	def __str__(self):
		return f"{self.message}"


class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        if self.balance-amount<0:
            raise LowBalanceError("initial balance is low")
        else:
            self.balance-=amount
            return self.balance

    def __str__(self):
        return f"This account belongs to {self.name} and has total {self.balance} amount in it."

if __name__=='__main__':
    anjal=Bank("anjal",100)
    print(anjal.deposit(100))
    print(anjal.withdraw(50))