import sqlite3

# Create database - create connection to non existing database
# If DB exists, it just connects to it
connection = sqlite3.connect('tutorial.db')
cursor = connection.cursor()


# Create table with name 'example' with columns Language, Version and Skill
def create_table():
    cursor.execute('CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT )')


# You can't create the same table twice
# create_table()


# Insert data into 'example' table
def enter_data():
    cursor.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    cursor.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    cursor.execute("INSERT INTO example VALUES('Python', 3.6, 'Intermediate')")
    cursor.execute("INSERT INTO example VALUES('Python', 3.4, 'Expert')")
    # Put changes from temporary file to DB
    connection.commit()


# enter_data()


def enter_dynamic_data(lang, version, skill):
    cursor.execute('INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)',
                   (lang, version, skill))
    connection.commit()


# lang = input('What language? ')
# version = float(input('What version? '))
# skill = input('What skill level? ')
# enter_dynamic_data(lang, version, skill)
# enter_dynamic_data('Python', 3.6, 'Intermediate')


def read_data():
    sql = "SELECT * FROM example"
    for row in cursor.execute(sql):
        print(row)
    print(20 * '#')


read_data()


def read_data_with_dynamic_query(language, skill_level):
    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"
    for row in cursor.execute(sql, [skill_level, language]):
        print(row)
    print(20 * '#')


# language = input('What language? ')
# level = input('What skill level? ')
# read_data_with_dynamic_query(language, level)
print('read Expert in Python')
read_data_with_dynamic_query('Python', 'Expert')


sql = "UPDATE example SET Skill = 'Inter' WHERE Skill = 'Intermediate'"
cursor.execute(sql)
print("Intermediate -> Inter")
read_data()

sql = "DELETE FROM example WHERE Skill = 'Inter'"
cursor.execute(sql)
print('Deleted with "Inter" skill level')
read_data()
connection.close()
