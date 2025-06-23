text = "The boy stood on the burning deck Whence all but he had fled"

print(text.split(" "))



def maketuple(variables, names):
  return (variables[n] for n in names)

def func():
  x = 23
  y = 45
  z = 67
  print(vars())
  return maketuple(vars(), 'x y z'.split())
  
print(func())
