## Module08 - Labs

The Python environment is supplied from a package known as Anaconda.  Currently it's not 'activated'

1. Activate the environment

    - You HAVE TO follow these steps exactly
    - Close ALL VS code windows
    - From the windows start button, find and launch a command prompt.  Type `command` into the search bar and that should lead you to it
    - type the command `anaconda3\scripts\activate` press return
    - WARNING, be sure to use '\\' in the command.  This is one place where Windows is picky about the right type of slash
    - without this the sqlite3 environment won't work properly
    - now STAY IN THE COMMAND PROMPT WINDOW and launch VS code by typing `code`
    - this launches VS Code under the activated environment

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

1. Replace the print with a loop
    - this allows you to iterate over each row of the returned data

1. Each returned row will be a sequence
    - unpack the row into individual data items
    - use code like `name, dob, itemsMade, payRate = row`

1. Experiment with using the data from the employee table to drive the calculation of employee pay that we did earlier in the course.
    - you might try adding new columns to the table and allowing individual employees to have customised bonus rates, and bonus thresholds (to do this go back to the `CREATE TABLE` line in the code to add the extra columns.  In the `INSERT INTO...` line you will need to add extra data values for those columns)
    - another thing you might try is to wrap the more complex payment logic into a function and into a module.  Import that module here to reuse the function.

## Bonus ideas

1. Just like a file, this code **should** close the connection object and the cursor object when it no longer needs them.  You could just add `.close()` calls

1. More sophisticated is to use a context manager.  Context managers interoperate with the Python `with` statement.  The `with` statement automates closing both at the end of the block **and** in the event of an exception

1. Adjust the connection creation to look like
    ```Python
    with contextlib.closing(sqlite3.connect("lab.db")) as con:
    ```
    you will need an `import contextlib` and you will need to indent all the following code

1. Simlarly adjust the cusor creation to look like
    ```Python
        with contextlib.closing(con.cursor()) as cur:
    ```
    you will need to indent all the following code

    **NOTE** The context manager requires a specific set of methods to do its work.  Known as the protocol.  The file object implements that protocol directly, which is why we could use file objects directly in the `with` statement.  The `sqlite3` objects don't follow that protocol to close the connection/cursor objects.  The `contextlib.closing` function wraps those objects to automate the `.close()` calls.  For further information see https://blog.rtwilson.com/a-python-sqlite3-context-manager-gotcha/ 
