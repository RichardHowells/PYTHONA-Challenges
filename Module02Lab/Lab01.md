## Lab01 - Basic data types

1. Define separate variables for each of
	- a variable initialized with an integer value
	- a variable initialized with a floating point value
	- a variable initialized with a boolean (True/False) value
1. For each of the variables print the type, and print the id 
	- use the `type()` function
	- use the `id()` function
1. Define another variable, initialized from your integer
1. Print its `id()`.  Notice that it's the same id as the original integer

### Calculating Pay

Jemima takes a job making widgets.  She is paid 50p for each widget she makes.

Write a program to calculate her pay for making 30 widgets, 40 widgets and 50 widgets.

You should use variables here.  It will make later parts of this challenge **much** easier.  Start with something like:

```
rate_per_widget = 0.50
quantity_made = 30

### Calculate the pay here

print(pay)

quantity_made = 40

### Repeat the calculation here.  Yes there is a better way than copy/paste but we have not taught it yet

print(pay)

### Repeat for the 50 quantity
```


Manually calculate the expected values and test that the program produces the results you expect

Extend that program so that for each widget after 35 Jemima is paid at a 50% higher rate per widget. You will have to do a little research on the `if` statement for this.  We have not formally covered the `if` statement.  Don't worry if you have trouble with it we will cover the `if` statement properly later on

Test it as above

Extend your code again so that after Jemima produces 45 widgets she gets a 10% bonus on her entire pay

Test it as above
