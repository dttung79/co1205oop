from w3_car import Car

class ShowRoom:
    def __init__(self, name):
        self.name = name
        self.cars = []      # init empty list of Car objects
    
    def add_car(self):
        id = int(input('Enter id: '))
        brand = input('Enter brand: ')
        price = int(input('Enter price: '))
        miles = int(input('Enter miles: '))
        # create a Car object
        car = Car(id, brand, price, miles)
        # add it to the list
        self.cars.append(car)

    def show_all(self):
        print(f'@@@@@ SHOW ROOM {self.name} @@@@@')
        for c in self.cars:
            c.show()

    def search_brand(self):
        brand = input('Enter brand to search: ')
        count = 0
        for c in self.cars:
            if brand.lower() == c.brand.lower():
                c.show()
                count += 1
        
        if count == 0:
            print(f'No car found for brand {brand}')

    def search_miles(self):
        miles = int(input('Enter miles to search: '))
        count = 0
        for c in self.cars:
            if c.miles <= miles:
                c.show()
                count += 1
        
        if count == 0:
            print(f'No car found less than {miles} miles')

    def search_price(self):
        price = int(input('Enter price to search: '))
        count = 0
        for c in self.cars:
            if c.price >= price:
                c.show()
                count += 1
        
        if count == 0:
            print(f'No car found greate than ${price}')

    def edit_car(self):
        id = int(input('Enter id to edit: '))
        found = False
        for c in self.cars:
            if c.id == id:
                new_price = int(input('Enter new price: '))
                new_miles = int(input('Enter new miles: '))
                c.price = new_price
                c.miles = new_miles
                print(f'Car ID {id} updated')
                found = True
        
        if not found:
            print(f'No car found for ID {id}')
    
    def delete_car(self):
        id = int(input('Enter id to edit: '))
        
        for i in range(len(self.cars)):
            if self.cars[i].id == id:
                self.cars.pop(i)
                print(f'Car ID {id} deleted')
                found = True
                return
        
        print(f'No car found for ID {id}')
    
    def print_menu(self):
        print('Welcom to Car Showroom')
        print('1. Show all cars')
        print('2. Search by brand')
        print('3. Search by price')
        print('4. Search by miles')
        print('5. Add new car')
        print('6. Edit car')
        print('7. Delete car')
    
    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:     self.show_all()
            elif choice == 2:   self.search_brand()
            elif choice == 3:   self.search_price()
            elif choice == 4:   self.search_miles()
            elif choice == 5:   self.add_car()
            elif choice == 6:   self.edit_car()
            elif choice == 7:   self.delete_car()
            elif choice == 0:   running = False


### Test
a5 = ShowRoom('A5')
a5.run()