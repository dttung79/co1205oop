class Car:
    def __init__(self, id, brand, price, miles):
        self.id = id
        self.brand = brand
        self.price = price
        self.miles = miles
    
    def show(self):
        print(f'Car {self.id} {self.brand}: ${self.price}, miles: {self.miles}')