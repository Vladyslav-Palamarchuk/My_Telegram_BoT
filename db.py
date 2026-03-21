import sqlite3

   # створюємо зєднання з баз.даних/ якщо файла не має, створюємо
def init_db():
    conn = sqlite3.connect("users_data.db")
    cursor = conn.cursor()
    #cursor = conn.cursor() - дозволяє робити SQL запити

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            user_id INTEGER,
            phone TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


def add_lead(user_name, user_id, phone):
    conn = sqlite3.connect("users_data.db")
    curses = conn.cursor()

    #записуємо дані в таблицю
    curses.execute(
        "INSERT INTO leads (user_name, user_id, phone) VALUES (?, ?, ?)",
        (user_name, user_id, phone)

    )

    conn.commit()
    conn.close()

