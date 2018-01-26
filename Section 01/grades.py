admins = {'python': 'password'}
grades = {}
is_auth = False


def log_in():
    global admins
    login = input('Username: ')
    if login not in admins:
        print('Invalid username')
    else:
        password = input('Password: ')
        if password != admins[login]:
            print('Invalid password')
        else:
            global is_auth
            is_auth = True


def log_out():
    global is_auth
    is_auth = False


def add_student():
    name = input('Student name: ')
    grade = float(input('Grade: '))
    global grades
    grades[name] = [grade]
    print('Added grade')


def remove_student():
    name = input('What student to remove: ')
    global grades
    try:
        del grades[name]
        print('Removed student')
    except Exception:
        print('No such student')


def get_average_grade(name):
    name = input('Student name: ')
    global grades
    try:
        scores = grades[name]
        return sum(scores)/len(scores)
    except Exception:
        print('No such student')


actions = {'1': add_student,
           '2': remove_student,
           '3': get_average_grade,
           '4': log_out}
