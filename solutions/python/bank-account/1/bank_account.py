class BankAccount:
    def __init__(self):
        self._isOpen = False
        self._balance = 0

    def get_balance(self):
        if self._isOpen:
            return self._balance
        else:
            raise ValueError("account not open")

    def open(self):
        if self._isOpen:
            raise ValueError('account already open')
        else:
            self._isOpen = True
            
    def deposit(self, amount):
        if not self._isOpen:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        else:
            self._balance += amount
            
    def withdraw(self, amount):
        if not self._isOpen:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        if amount > self._balance:
            raise ValueError('amount must be less than balance')
        else:
            self._balance -= amount
            
    def close(self):
        if not self._isOpen:
            raise ValueError('account not open')
        else:
            self._isOpen = False
            self._balance = 0
