import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""

INSERT INTO students(
name,
age
)

VALUES(
?,
?
)

""",

("Samiullah",25)

)

conn.commit()

print("Student Added")

conn.close()