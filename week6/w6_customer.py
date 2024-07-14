class Customer:
    __id = 0
    def __init__(self, name):
        self.name = name
        self.bill = 0
        self.__id = Customer.__id
        Customer.__id += 1

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def bill(self):
        return self.__bill
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value

    @bill.setter
    def bill(self, value):
        if value < 0:
            raise ValueError('Bill must be positive')
        self.__bill = value

    def print_receipt(self):
        print(f'Receipt for customer {self.name}, ID: {self.id}')
        print(f'Bill: ${self.bill}')
        print(f'Payment: ${self._payment():.2f}')
    
    def _payment(self):
        return self.bill * 1.1

class VIPCustomer(Customer):
    def __init__(self, name, rank):
        super().__init__(name)
        self.rank = rank    

    @property
    def rank(self):
        return self.__rank
    
    @rank.setter
    def rank(self, value):
        if value.lower() != 'silver' and value.lower() != 'gold':
            raise ValueError('Invalid rank!')
        self.__rank = value.lower()
    
    def _payment(self):
        if self.rank == 'silver':
            return self.bill * 0.95
        else:
            return self.bill * 0.85
        
### TEST
c = Customer('Alice')
c.bill = 100
c.print_receipt()

v1 = VIPCustomer('Bob', 'silver')
v1.bill = 100
v1.print_receipt()

v2 = VIPCustomer('Charlie', 'gold')
v2.bill = 100
v2.print_receipt()