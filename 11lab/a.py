import psycopg2,re

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = 'Dat2022Pyth')

current = conn.cursor()

pagination = """ 

SELECT * FROM phonebook LIMIT %s OFFSET %s; 

""" 


search = """ 
CREATE OR REPLACE FUNCTION search(name VARCHAR) 
    RETURNS TABLE (person_name VARCHAR, person_surname VARCHAR, phone_number VARCHAR) 
    AS $$ 
BEGIN 
    RETURN QUERY SELECT * FROM phonebook WHERE phonebook.person_name ILIKE name OR phonebook.person_surname ILIKE name OR phonebook.person_number ILIKE name; 
END; 
$$ 
LANGUAGE PLPGSQL; 

SELECT * FROM search (%s); 
""" 


update = '''
    create or replace procedure update(name varchar,surname varchar,number varchar)
        as $$
            begin
                if exists(select * from phonebook where person_name = name) then
                    update phonebook set person_number = number where person_name = name;
                else
                    insert into phonebook values(name,surname,number);
                end if;
            end;
        $$ language plpgsql;

        call update(%s, %s, %s);
'''


insert = ''' 
    create or replace procedure insert(name varchar, surname varchar, number varchar)
    as $$
    begin
        insert into phonebook values(name,surname,number);
    end; $$ 
    language plpgsql; 
    CALL insert(%s,%s,%s);  
'''


delete = """ 
CREATE OR REPLACE PROCEDURE deleteT(name VARCHAR) 
AS $$ 
BEGIN 
    DELETE FROM phonebook WHERE person_name = name OR person_surname = name OR person_number = name; 
END; $$ 
LANGUAGE PLPGSQL; 
CALL deleteT(%s); 
""" 

def check(s): 

    return bool(re.match(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", s)) 




while True: 

    command = input("search, insert, pagination, delete, exit\n") 




    if command == 'search':

        n = input("Введите часть: ")

        word = '%' + n + '%'

        current.execute(search, [word])

        print(*current.fetchall(), sep="\n")







    if command == 'insert':

        n = int(input("How many users do you want to add? "))

        for i in range(n):

            name = str(input())

            surname = str(input())

            number = str(input())

            if check(number):

                current.execute(update,(name,surname,number))

            else:

                print('Number is incorrect! Please try again!')

        conn.commit()




    if command == 'pagination': 

        a, b = map(int, input("LIMIT, OFFSET: ").split()) 

        current.execute(pagination, (a, b)) 

        print(*current.fetchall(), sep = '\n') 

        

    if command == 'delete':

        n = input("Введите имя или фамилию или номер чтобы удалить: ")

        current.execute(delete,[n])

        conn.commit()




    if command == 'exit':

        break







current.close()

conn.commit()

conn.close()