
def basic_pay(rate, items):
    return rate * items


for items in [30, 40, 50]:
    print(basic_pay(0.5, items)) 

print([basic_pay(0.5, items) for items in [30, 40, 50]])   

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)
    
print(factorial(1))
print(factorial(5))