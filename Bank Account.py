class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited, your current balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn, your current balance is {self.balance}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

account1 = BankAccount("Surya", 20000)
account2 = BankAccount("Dhiraj", 150000)

account1.deposit(15000)
account1.withdraw(6000)
account1.check_balance()