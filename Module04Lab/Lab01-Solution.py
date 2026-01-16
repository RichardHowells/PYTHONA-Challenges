
def basic_pay(rate_per_widget, quantity_made, enhancement_threshold = 35):
    if quantity_made > enhancement_threshold:
        excess_units = quantity_made - enhancement_threshold
        excess_pay = excess_units * rate_per_widget * 0.5
    else:
        excess_pay = 0

    basic_pay = quantity_made * rate_per_widget
    pay = basic_pay + excess_pay

    if quantity_made > 45:
        pay = pay * 1.1

    return pay


quantities = [30, 40, 50]

print("Calling from for loop")
for quantity in quantities:
    print(basic_pay(0.5, quantity)) 

print("Calling from list comprehension")
print([basic_pay(0.5, quantity) for quantity in quantities])   

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(1))
print(factorial(5))