import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

persons = [
    ("test1", "test2"),
]

c.execute("CREATE TABLE first (firstname, lastname)")

c.executemany("INSERT INTO first(firstname, lastname) VALUES (?, ?)", persons)

for row in c.execute("SELECT * FROM first;"):
    print(row)