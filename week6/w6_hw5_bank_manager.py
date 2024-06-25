from w6_hw5_account import Account
from w6_hw5_bank import Bank

class BankManager:
    def __init__(self, name):
        self.__bank = Bank(name)
    
    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = input('Enter your choice: ')
            if choice == 1:     self._add_account()
            elif choice == 2:   self._remove_account()
            elif choice == 3:   self._withdraw()
            elif choice == 4:   self._deposit()
            elif choice == 5:   self._show()
            elif choice == 6:   self._show_all()
            elif choice == 0:   running = False
            else:               print('Invalid choice')
    
    def __print_menu(self):
        print('1. Add account')
        print('2. Remove account')
        print('3. Withdraw')
        print('4. Deposit')
        print('5. Show')
        print('6. Show all')
        print('0. Quit')

    def _add_account(self):
        try:
            name = input('Enter account name: ')
            balance = float(input('Enter account balance: '))
            acc = Account(name, balance)
            self.__bank.add(acc)
            print('Account added')
        except ValueError as e:
            print('Error:', e)