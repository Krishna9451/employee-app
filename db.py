import os
import psycopg2

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
)
""")

conn.commit()

cursor.execute(
    "INSERT INTO employees(name) VALUES(%s)",
    ("Krishna",)
)

conn.commit()

cursor.execute("SELECT * FROM employees")

employees = cursor.fetchall()

for emp in employees:
    print(emp)
