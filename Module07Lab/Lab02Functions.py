
print("Hello from functions")

def square(x):
    return x * x

def tupleAppender(t, newItem):
    tupleAsList = list(t)
    tupleAsList.append(newItem)
    return tuple(tupleAsList)
    