import Lab02Functions

print("About to call square")

print(Lab02Functions.square(99))

print(Lab02Functions.tupleAppender((1, 2, 3), "fred"))

# Note these subsequent imports do NOT print the message from Lab02Functions 
import Lab02Functions as fns
print(fns.square(99))

# Note these subsequent imports do NOT print the message from Lab02Functions 
from Lab02Functions import square
print(square(99))
