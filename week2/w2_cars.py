cars = {1: ['Honda', 'Civic', 10000, 0],
        2: ['Toyota', 'Lexus', 500000, 10000],
        3: ['Honda', 'CX5', 15000, 200],
        4: ['Hyunda', 'Kona', 8000, 5000]}

def print_menu():
    print('Welcom to Car Showroom')
    print('1. Show all cars')
    print('2. Search by brand')
    print('3. Search by price')
    print('4. Search by miles')
    print('5. Add new car')
    print('6. Edit car')
    print('7. Delete car')

def show_all():
    print('All cars in showroom')
    for car_id, car_info in cars.items():
        print_car(car_id, car_info)

def search_brand():
    brand = input('Enter a brand to search: ')

    for car_id, car_info in cars.items():
        if brand.lower() == car_info[0].lower():
            print_car(car_id, car_info)

def print_car(car_id, car_info):
    print(f'{car_id} {car_info[0]} {car_info[1]} ${car_info[2]}, ODO {car_info[3]} miles')

def search_price():
    price = int(input('Enter a price to search: '))
    
    count = 0
    for car_id, car_info in cars.items():
        if car_info[2] >= price:
            print_car(car_id, car_info)
            count += 1
    
    if count == 0:
        print(f'No car has price >= {price}')

def search_miles():
    miles = int(input('Enter minimum miles to search: '))
    count = 0

    for car_id, car_info in cars.items():
        if car_info[3] <= miles:
            print_car(car_id, car_info)
            count += 1

    if count == 0:
        print(f'There is no car has miles <= {miles}')

def add_car():
    car_id = int(input('Enter new car id: '))
    
    if car_id in cars:
        print(f'Car id {car_id} existed! Please enter new id')
        return
    
    brand = input('Enter new car brand: ')
    model = input('Enter new car model: ')
    price = int(input('Enter new car price: '))
    miles = int(input('Enter new car miles: '))

    cars[car_id] = [brand, model, price, miles]
    print(f'New car added.')

def edit_car():
    car_id = int(input('Enter old car id to edit: '))
    if car_id not in cars:
        print(f'Car id {car_id} not existed! Please enter exist id')
        return
    
    car_info = cars[car_id]
    car_info[2] = int(input('Enter new price: '))
    car_info[3] = int(input('Enter new miles: '))

    print(f'Car {car_id} updated!')

def delete_car():
    car_id = int(input('Enter old car id to edit: '))
    if car_id not in cars:
        print(f'Car id {car_id} not existed! Please enter exist id')
        return
    
    cars.pop(car_id)
    print(f'Car {car_id} deleted!')

def run():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:     show_all()
        elif choice == 2:   search_brand()
        elif choice == 3:   search_price()
        elif choice == 4:   search_miles()
        elif choice == 5:   add_car()
        elif choice == 6:   edit_car()
        elif choice == 7:   delete_car()
        elif choice == 0:   running = False  
        else:               print('Invalid choice!')
    print('See you again!')

#### MAIN ####
run()