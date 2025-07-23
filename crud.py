import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()



def insert_user(name, age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()

def update_user(name, new_age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name))
    conn.commit()
    conn.close()

def get_users(age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE age > ?', (age,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def main():
    create_table()
    insert_user('Alice', 30)
    insert_user('Bob', 25)
    insert_user('Charlie', 35)
    insert_user('David', 28)
    insert_user('Eve', 22)

    update_user('Alice', 31)

    users_above_30 = get_users(30)
    for user in users_above_30:
        print(user)

if __name__ == "__main__":
    main()
