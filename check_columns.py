import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(total_sales)")
columns = cursor.fetchall()

for col in columns:
    print(col)

conn.close()
