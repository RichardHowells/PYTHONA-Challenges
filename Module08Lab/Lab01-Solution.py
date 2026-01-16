import sqlite3
con = sqlite3.connect("lab.db")
cur = con.cursor()

# This line will get rid of the table. 
# it will NOT crash if the table is missing
cur.execute("DROP TABLE IF EXISTS employee")

# This line will crash if the database table is already present
cur.execute("CREATE TABLE employee(name, DOB, itemsMade, payRate)")
cur.execute("""
    INSERT INTO employee VALUES
        ('Jemima Puddleduck', 2001, 50, 0.5),
        ('Rupert Bear', 1971, 100, 0.4)
""")

con.commit()

res = cur.execute("SELECT * FROM employee")
print(res.fetchall())

# It's a best practice to specify just the columns you actually want
res = cur.execute("SELECT name, DOB, itemsMade, payRate FROM employee")
for row in res:
    # This is a place where we get given a tuple for each row
    # First unpack that into meaningful names
    name, dob, itemsMade, payRate = row

    basic_pay = itemsMade * payRate
    
    print(name, "is paid", basic_pay)