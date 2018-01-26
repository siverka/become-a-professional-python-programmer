admins = {'admin': 'password'}
grades_database = {}
is_auth = False

# Log in to database
def log_in():
    global admins
    login = input('Username: ')
    if login not in admins:
        print('Invalid username')
        return False
    else:
        password = input('Password: ')
        if password != admins[login]:
            print('Invalid password')
            return False
    return True


def add_student():
    student = input('Student : ')
    grade = float(input('Grade: '))
    global grades_database

    if student in grades_database:
        grades_database[student].append(grade)
    else:
        grades_database[student] = [grade]
    print('Added grade')


def remove_student():
    student = input('What student to remove: ')
    global grades_database
    try:
        del grades_database[student]
        print('Removed student')
    except Exception:
        print('No such student')


def get_average_grade():
    student = input('Student name: ')
    global grades_database
    try:
        grades = grades_database[student]
        print(sum(grades)/len(grades))
    except Exception:
        print('No such student')


actions = {'1': add_student,
           '2': remove_student,
           '3': get_average_grade}

def main():
    print('''
        Welcome to Grade Central
        
        [1] - Enter grades
        [2] - Remove student
        [3] - Student average grades
        [4] - Exit
    ''')
    global actions
    if log_in():
        action = input('What would you like to do today? (Enter a number) ')
        while action in actions:
            actions[action]()
            print(grades_database)
            action = input('What would you like to do today? (Enter a number) ')

main()
