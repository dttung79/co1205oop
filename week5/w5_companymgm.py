from w5_employee import Employee
from w5_company import Company

class CompanyManagerProgram:
    def __init__(self, name):
        self.__company = Company(name)
    
    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = input("Enter choice: ")
            if choice == "1":       self.__add_employee()
            elif choice == "2":     self.__remove_employee()
            elif choice == "3":     self.__change_employee_rate()
            elif choice == "4":     self.__show_employee()
            elif choice == "5":     self.__show_all_employees()
            elif choice == "0":     running = False
            else:                   print("Invalid choice")
    
    def __print_menu(self):
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Change employee rate")
        print("4. Show employee")
        print("5. Show all employees")
        print("0. Exit")
    def __add_employee(self):
        try:
            id = int(input("Enter employee ID: "))
            name = input("Enter employee name: ")
            rate = float(input("Enter employee rate: "))
            e = Employee(id, name, rate)
            self.__company.add(e)
            print("Employee added")
        except ValueError as err:
            print(err)

    def __remove_employee(self):
        try:
            id = int(input("Enter employee ID: "))
            self.__company.remove(id)
            print("Employee removed")
        except ValueError as err:
            print(err)
    
    def __change_employee_rate(self):
        try:
            id = int(input("Enter employee ID: "))
            new_rate = float(input("Enter new rate: "))
            self.__company.change(id, new_rate)
            print("Employee rate changed")
        except ValueError as err:
            print(err)
    
    def __show_employee(self):
        try:
            id = int(input("Enter employee ID: "))
            self.__company.show_employee(id)
        except ValueError as err:
            print(err)
    
    def __show_all_employees(self):
        self.__company.show_all()

if __name__ == "__main__":
    name = input("Enter company name: ")
    program = CompanyManagerProgram(name)
    program.run()