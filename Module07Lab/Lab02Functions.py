'''
The Docstring for Lab02Functions

Here is where we describe what the file is about
'''

print("Hello from functions")

def square(x):
    "It's common to triple quote a docstring, but not required. This function takes in a number and returns its square"
    return x * x

def tupleAppender(t, newItem):
    tupleAsList = list(t)
    tupleAsList.append(newItem)
    return tuple(tupleAsList)
    