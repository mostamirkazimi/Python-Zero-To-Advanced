import sqlite3

# اتصال به دیتابیس
conn = sqlite3.connect("students.db")

cursor = conn.cursor()

# ساخت جدول
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# ذخیره تغییرات
conn.commit()

print("Table Created")

conn.close()