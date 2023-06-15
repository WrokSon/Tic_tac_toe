
import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

try:
    cursor.execute("""
    SELECT * FROM users WHERE id = 1
    """,())
    print(cursor.fetchone())
except:
    pass  
my_username = ("marc,")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

connection.close()


