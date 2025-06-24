import sqlite3
con = sqlite3.connect("lab.db")
cur = con.cursor()

# This line will get rid of the table. 
# it will NOT crash if the table is missing
cur.execute("DROP TABLE IF EXISTS employee")

# This line will crash if the database table is already present
cur.execute("CREATE TABLE employee(name, DOB, payRate)")
cur.execute("""
    INSERT INTO employee VALUES
        ('Jemima Puddleduck', 2001, 0.5),
        ('Rupert Bear', 1971, 0.4)
""")
con.commit()
res = cur.execute("SELECT * FROM employee")
print(res.fetchall())