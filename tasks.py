import sqlite3

conn = sqlite3.connect("tasks.db")
conn.execute(
    "CREATE TABLE IF NOT EXISTS tasks ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "title TEXT NOT NULL, "
    "done INTEGER NOT NULL DEFAULT 0)"
)

def add_task(title):
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()

def list_tasks():
    return conn.execute("SELECT id, title, done FROM tasks").fetchall()

if __name__ == "__main__":
    add_task("Learn SQL")
    for task in list_tasks():
        print(task)