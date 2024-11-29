class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Current balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance < amount:
            return "Error: Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. Current balance: {self.balance}"

    def check_balance(self):
        return f"Current balance: {self.balance}"

if __name__ == "__main__":
    my_bank = Bank()
    print(my_bank.deposit(100))
    print(my_bank.withdraw(50))
    print(my_bank.check_balance())
    print(my_bank.withdraw(100))