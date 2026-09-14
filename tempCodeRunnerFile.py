class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited, your current balance is {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawn, your current balance is {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

owner1 = BankAccount("Surya", 20000)
owner2 = BankAccount("Dhiraj", 150000)

owner1.deposit(15000)
owner1.withdraw(6000)
owner1.balance()