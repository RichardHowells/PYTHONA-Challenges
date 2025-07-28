i = 10
print(type(i), id(i))

j = 1.1
print(type(j), id(j))

k = True
print(type(k), id(k))

l = i
print(type(l), id(l))

rate_per_widget = 0.50
quantity_made = 30

pay = quantity_made * rate_per_widget

print(pay)

quantity_made = 40

### Repeat the calculation here.  Yes there is a better way than copy/paste but we have not taught it yet

pay = quantity_made * rate_per_widget

print(pay)

### Repeat for the 50 quantity

quantity_made = 50

pay = quantity_made * rate_per_widget

print(pay)

### With higher pay over 35 units - expected result 28.75

quantity_made = 50

if quantity_made > 35:
    excess_units = quantity_made - 35
    excess_pay = excess_units * rate_per_widget * 0.5
else:
    excess_pay = 0

basic_pay = quantity_made * rate_per_widget
pay = basic_pay + excess_pay
    
print("Higher pay over 35 units", pay)

### Over 45 units - With a 10% bonus on entire pay - expected 31.625
# note that the actual shows a rounding error 

quantity_made = 50

if quantity_made > 35:
    excess_units = quantity_made - 35
    excess_pay = excess_units * rate_per_widget * 0.5
else:
    excess_pay = 0

basic_pay = quantity_made * rate_per_widget
pay = basic_pay + excess_pay

if quantity_made > 45:
    pay = pay * 1.1
    
print(pay)
