list_ids = [1, 2, 3, 4, 5]
list_titles = ['Cambridge', 'Road to IELTS', 'Harry Potter', 'Sherlock Homes', 'The Godfather']
list_authors = ['Ronaldo', 'Tommy', 'Foden', 'Brian', 'David']
list_statuses = ['available', 'available', 'available', 'available', 'available']

def run():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:     add_book()
        elif choice == 2:   search_book()
        elif choice == 3:   edit_book()
        elif choice == 4:   delete_book()
        elif choice == 5:   display_all_books()
        elif choice == 6:   borrow_book()
        elif choice == 0:   running = False
        else:               print('Invalid choice! Please choose again')
    
    print('Thank you for using Book Management System!')

def print_menu():
    print('+++++++ BOOK MANAGEMENT SYSTEM +++++++')
    print('1. Add book')
    print('2. Search book')
    print('3. Edit book')
    print('4. Delete book')
    print('5. Display all books')
    print('6. Borrow book')
    print('0. Exit')

def add_book():
    print('Add new book: ')
    
    id = int(input('Enter a new book ID: '))
    pos = check_id(id)
    if pos != -1:  # -1 means not found
        print(f'Book id {id} exists. Please choose a different ID')
        return
    
    title = input('Enter new book title: ')
    author = input('Enter new book author: ')

    list_ids.append(id)
    list_titles.append(title)
    list_authors.append(author)
    list_statuses.append('available')

    print(f'Book "{title}" added successfully!')

def check_id(id):
    for i in range(len(list_ids)):
        if list_ids[i] == id:
            return i
    return -1

def search_book():
    id = int(input('Enter the book ID: '))
    pos = check_id(id)
    if pos == -1:
        print(f'No book found with ID {id}')
        return

    print_book(list_ids[pos], list_titles[pos], list_authors[pos], list_statuses[pos])

def edit_book():
    id = int(input('Enter book ID to edit: '))
    pos = check_id(id)
    
    if pos == -1:
        print(f'Book ID {id} not found. Please choose a different ID')
        return
    
    list_titles[pos] = input('Enter new title: ')
    list_authors[pos] = input('Enter new author: ')
    
    print(f'Updated book ID {id}: Title: {list_titles[pos]}, Author: {list_authors[pos]}')

def delete_book():
    id = int(input('Enter book ID to delete: '))
    pos = check_id(id)

    if pos == -1:
        print(f'Book ID {id} not found. Please choose a different ID')
        return
    
    list_ids.pop(pos)
    list_authors.pop(pos)
    list_titles.pop(pos)
    list_statuses.pop(pos)

    print(f'Book ID {id} deleted successfully!')

def display_all_books():
    print('All books and their details:')
    for i in range(len(list_ids)):
        print_book(list_ids[i], list_titles[i], list_authors[i], list_statuses[i])

def print_book(id, title, author, status):
    print(f'Book ID: {id}, Title: {title}, Author: {author}, Status: {status}')

def borrow_book():
    id = int(input('Enter the book ID to borrow: '))
    pos = check_id(id)

    if pos == -1:
        print(f'No book found with ID {id}')
        return
    
    if list_statuses[pos] == 'not available':
        print(f'Book ID {id} is currently not available')
        return
    
    list_statuses[pos] = 'not available'
    print(f'Book ID {id} has been borrowed')

run()