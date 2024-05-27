list_ids = [1, 2, 3]
list_names = ['John', 'Alain', 'Donald']
list_subjects = ['Network, Security', 'Python, C++, Network', 'C++, Web Develop, Java']

def run():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter you choice: '))
        if choice == 1:
            add_teacher()
        elif choice == 2:
            edit_teacher()
        elif choice == 3:
            delete_teacher()
        elif choice == 4:
            show_all()
        elif choice == 5:
            search_teacher()
        elif choice == 0:
            print('Thank you for using Teacher Management Application!')
            running = False
        else:
            print('Invalid choice! Please choose again')

def print_menu():
    print('++++++++++ TEACHER MANAGEMENT ++++++++++')
    print('1. Add teacher')
    print('2. Edit teacher')
    print('3. Delete teacher')
    print('4. Show all teachers')
    print('5. Search teacher')

def add_teacher():
    print('Add new teaher')
    id = int(input('Enter new teacher id: '))
    
    pos = check_id(id)
    if pos != -1:   # -1 means not found
        print(f'Teacher ID {id} exist. Please choose a different ID')
        return 
    
    name = input('Enter new teacher name: ')
    subjects = input('Enter a list of subjects, separate by comma: ')

    list_ids.append(id)
    list_names.append(name)
    list_subjects.append(subjects)
    print(f'Teacher {name} added succesfully!')

def check_id(id):
    for i in range(len(list_ids)):
        if list_ids[i] == id:
            return i
    # not found
    return -1

def edit_teacher():
    id = int(input('Enter teacher id to edit: '))
    pos = check_id(id)
    
    if pos == -1:   # -1 means not found
        print(f'Teacher ID {id} not found. Please choose a different ID')
        return 
    
    new_subjects = input('Enter new subjects (split by comma): ')
    list_subjects[pos] = new_subjects
    print(f'Updated subjects for teacher ID {id}')

def delete_teacher():
    id = int(input('Enter teacher id to delete: '))
    pos = check_id(id)
    
    if pos == -1:
        print(f'Teacher ID {id} not found. Please choose a different ID')
        return
    
    list_ids.pop(pos)
    list_names.pop(pos)
    list_subjects.pop(pos)
    print(f'Teacher ID {id} deleted succesfully!')

def show_all():
    print('All teachers & their subjects')
    for i in range(len(list_ids)):
        print(f'Teacher ID: {list_ids[i]}, name: {list_names[i]}')
        print(f'Subjects: {list_subjects[i]}')

def search_teacher():
    subject = input('Enter a subject')
    print(f'List of teacher who can teach {subject}:')
    count = 0
    for i in range(len(list_subjects)):
        if subject in list_subjects[i]:
            print(f'Teacher ID: {list_ids[i]}, name: {list_names[i]}')
            count += 1

    if count == 0:
        print(f'No teacher available for subject {subject}')

### RUN MAIN PROGRAM ####
run()