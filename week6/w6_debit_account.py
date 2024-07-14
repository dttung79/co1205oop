from w6_hw5_account import Account

class DebitAccount(Account):
    def __init__(self, name, balance, limit):
        super().__init__(name, balance)
        self.limit = limit
    
    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, limit):
        if limit <= 0:
            raise ValueError('Limit must be positive')
        self.__limit = limit
    
    def withdraw(self, amount):
        if amount > self.balance + self.limit:
            raise ValueError('Insufficient balance')
        if amount <= 0:
            raise ValueError('Amount must be positive')
        self._set_balance(self.balance - amount)

    def show(self):
        super().show()
        print(f'Account debit limit: ${self.limit}')