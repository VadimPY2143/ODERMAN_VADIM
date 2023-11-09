import sqlite3

try:
    sqlite_connection = sqlite3.connect("sqlite_python_oderman2.db")
    cursor = sqlite_connection.cursor()
    print('DB created and connected')
    sqlite_select_query = 'SELECT sqlite_version();'
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print('SQLite versions: ', record)
    cursor.close()
except sqlite3.Error as error:
    print('Error: ',error)

finally:
    if sqlite_connection:
        sqlite_connection.commit()
        print('DB disconnected')


try:
    sqlite_connection = sqlite3.connect("sqlite_python_oderman2.db")
    sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS sqlitedb_oderman (
                                    name TEXT,
                                    price INTEGER); '''
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('Table Created')
    cursor.close()

except sqlite3.Error as error:
    print('Error: ', error)

finally:
    if sqlite_connection:
        sqlite_connection.commit()
        print('DB disconnected')

try:
    sqlite_connection = sqlite3.connect("sqlite_python_oderman2.db")
    sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS order_db (
                                    pizza_name TEXT,
                                    pizza_count INTEGER,
                                    delivery_adress TEXT,
                                    phone_number TEXT); '''
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('Table Created')
    cursor.close()

except sqlite3.Error as error:
    print('Error: ', error)

finally:
    if sqlite_connection:
        sqlite_connection.commit()
        print('DB disconnected')




def insert_to_database(name, price):
    try:
        sqlite_connection = sqlite3.connect("sqlite_python_oderman2.db")
        cursor = sqlite_connection.cursor()
        sqlite_insert_param = ''' INSERT INTO sqlitedb_oderman
                                (name,price)
                                VALUES
                                (?,?);'''
        data_tuple = (name,price)

        cursor.execute(sqlite_insert_param, data_tuple)
        print('INSERTED')
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print('Error: ', error)

    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            print('DB disconnected')




insert_to_database('Гавайська', 200)
insert_to_database('Салямі', 249)
insert_to_database('Пеппероні', 250)
insert_to_database('Карбонара', 300)



