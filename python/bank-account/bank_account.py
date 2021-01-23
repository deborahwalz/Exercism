import threading

class BankAccount:
    def __init__(self):
        self.opened = False
        self.lock = threading.Lock()

    def get_balance(self):
        if not self.opened:
            raise ValueError("Account is closed!")
        return self.balance

    def open(self):
        if self.opened:
            raise ValueError("Account is already opened!")
        self.opened = True
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount!")
        elif not self.opened:
            raise ValueError("Account is closed!")
        else:
            with self.lock:
                self.balance += amount

    def withdraw(self, amount):
        if (amount <= 0) or (amount > self.balance):
            raise ValueError("Invalid amount!")
        elif not self.opened:
            raise ValueError("Account is closed!")
        else:
            with self.lock:
                self.balance -= amount

    def close(self):
        if not self.opened:
            raise ValueError("Account is closed!")
        self.opened = False
