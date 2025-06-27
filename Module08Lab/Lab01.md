## Module08 - Labs

The Python environment is supplied from a package known as Anaconda.  Currently it's not 'activated'

1. Activate the environment

    - at a command prompt type
    `anaconda3\scripts\activate` press return
    - WARNING, be sure to use '\' in the command.  This is one place where Windows is picky about the right type of slash
    - without this the sqlite3 environment won't work properly

1. Sqlite3 is a lightweight database and is part of the Python standard library

1. Paste this code into a python file

    ```Python
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
    ```

1. Experiment with using data from the employee table to drive the calculation of employee pay that we did earlier in the course.
    - you might try adding new columns to the table and allowing individual employees to have customised bonus rates, and bonus thresholds

