import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS login(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    FOREIGN KEY (userId) references users(id)
)
''')
users = [
    ("Jeff", 20),
    ("Jake", 22),
    ("Alice", 24)
]
login = [
    (1, "jeffff", "passsfds"),
    (2, "jakeeee", "passfdsfdsf"),
    (3, "Aliceeee", "passfdsfdsfds")
]
cursor.executemany("INSERT INTO users(name, age) VALUES(?,?)", users)
conn.commit()

cursor.executemany("INSERT INTO login(userId, username, password) VALUES(?,?,?)", login)
conn.commit()

def getUsers():
    cursor.execute("SELECT * FROM USERS")
    return cursor.fetchall()

def getLogin():
    cursor.execute("SELECT * FROM LOGIN")

    return cursor.fetchall()

def getUsersWithLogin():
    cursor.execute('''SELECT users.id, users.name, users.age, login.username, login.password
    FROM users
    JOIN login ON users.id = login.userId; ''')
    return cursor.fetchall()


print(getUsers())
print(getLogin())
print(getUsersWithLogin())