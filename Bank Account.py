class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited, your current balance is {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                       self.__balance -= amount
                       print(f"{amount} withdrawn, your current balance is {self.__balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdraw amount")

    def check_balance(self):
        print(f"Current balance: {self.__balance}")

account1 = BankAccount("Surya", 20000)
account2 = BankAccount("Dhiraj", 150000)

account1.deposit(15000)
account1.withdraw(6000)
account1.check_balance()