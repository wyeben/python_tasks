import sqlite3

try:
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                      (id INTEGER PRIMARY KEY,
                       name TEXT,
                       age INTEGER)''')

    cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ("Yila Benson", 20))

    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()

    for row in results:
        print(row)

    connection.commit()
    connection.close()

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
