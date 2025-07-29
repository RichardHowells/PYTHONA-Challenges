## Lab02 Modules

1. Create a module
    - A file named `functions.py`
    - add a print call like
        `print("Hello from functions.py")`
    - add a function named `square` that takes a number and returns the square

1. Create another file
    - named `caller.py`
    - add an import for the functions module
    `import functions` note there is no .py
    - add a line
        `print("about to call square")`
    - call the `square` function in the functions module using the fully qualified name...
    `fourSquared = functions.square(4)`
    `print(fourSquared)`

1. Run and test
    - note that when the module is imported all 'unenclosed code' (code not in a function) is executed hence the `Hello` message is seen when the import is executed
    - It's a bad practice to have unenclosed code in a module that gives an intrusive effect.  Ie don't print anything!

### Bonus Ideas
1. Extend the module with a function, `tupleExtender` that expects a tuple and a newItem as parameters.  It appends `newItem`to the tuple and then returns it. Tuples are immutable so you have to
    - convert the tuple to a list
    - append to the list
    - convert the list back to a new tuple
    - return the new tuple

1. Add a call to the `tupleExtender` to test it

1. Experiment with importing the module using an alias
    - `import functions as fns`

1. Experiment with importing an individual function into the current namespace
    - `from functions import square`
    - now it's callable without qualification
    - `sq = square(4)`

