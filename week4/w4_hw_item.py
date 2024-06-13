class Item:
    def __init__(self, id, name, price, quantity):
        self.__set_id(id)
        self.set_name(name)
        self.set_price(price)
        self.__quantity = 0
        self.add(quantity)
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    # set_id is private to hide it from outside
    def __set_id(self, id):
        if id < 0:
            print("ID must be positive")
            self.__id = 0   # use default value in case of invalid input
            return
        self.__id = id

    def set_name(self, name):
        if name == '':
            print("Name cannot be empty")
            self.__name = 'No Name'
            return
        self.__name = name

    def set_price(self, price):
        if price < 0:
            print("Price must be positive")
            self.__price = 0
            return
        self.__price = price

    def add(self, quantity):
        if quantity < 0:
            print("Quantity must be positive")
            return
        self.__quantity += quantity

    def remove(self, quantity):
        if quantity < 0:
            print("Quantity must be positive")
            return
        if quantity > self.__quantity:
            print("Not enough quantity to remove")
            return
        self.__quantity -= quantity

    def show(self):
        print(f"ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Quantity: {self.__quantity}")
    
