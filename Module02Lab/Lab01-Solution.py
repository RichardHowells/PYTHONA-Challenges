i = 10
print(type(i), id(i))

j = 1.1
print(type(j), id(j))

k = True
print(type(k), id(k))

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

### With a bonus over 35 units

quantity_made = 50
pay = quantity_made * rate_per_widget

if quantity_made > 35:
    excess_units = quantity_made - 35
    excess_pay = quantity_made * rate_per_widget * 0.5

basic_pay = quantity_made * rate_per_widget
pay = basic_pay + excess_pay
    
print(pay)
