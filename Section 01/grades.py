admins = {'admin': 'password'}
grades_database = {'Alex': [92, 76, 88],
                   'Jeff': [78, 88, 93, 100],
                   'Sam': [89, 92, 93]
                   }
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


def add_grade():
    student = input('Student name: ')
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
        print('Student does not exist')


def get_average_grades():
    global grades_database
    for student in grades_database:
        grades = grades_database[student]
        avg = sum(grades)/len(grades)
        print('{} has an average grade of: {:.2f}'.format(student, avg))


actions = {'1': add_grade,
           '2': remove_student,
           '3': get_average_grades,
           '4': exit}

info = '''
    Welcome to Grade Central
    
    [1] - Enter grades
    [2] - Remove student
    [3] - Student average grades
    [4] - Exit
'''

def main():

    global actions
    global info
    if log_in():
        while True:
            print(info)
            action = input('What would you like to do today? (Enter a number) ')
            if action in actions:
                actions[action]()
                print(grades_database)
            else:
                print('No valid choice was given, try again')


main()
