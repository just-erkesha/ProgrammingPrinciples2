import psycopg2

conn = psycopg2.connect(    
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = 'Dat2022Pyth'
    )
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTs PhoneBook1 (user_name text unique, phone text unique)')

delete_name = input('enter name you want delete...\n')

try:
    cursor.execute(f'delete from phonebook1 where user_name = \'{delete_name}\';')
except:
    print('this name does not exist')


cursor.execute('select * from PhoneBook1')
print(cursor.fetchall())
conn.commit()
cursor.close()
conn.close()

