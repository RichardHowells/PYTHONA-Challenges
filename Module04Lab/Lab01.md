## Lab01 - Functions

### Refactoring

Refactoring is a general word for changing (to improve!) the design of a piece of code whilst preserving what it does.

Go back to your code for Jemima's payment calculation

Extract the payment calculation into a function.  Your function should take in rate_per_widget and quantity_made.  It should return the calculated pay

Call this function from a `for` loop that iterates over a list containing the quantities that Jemima makes

Try repeating that logic as a list comprehension

### Bonus steps

Make your function more flexible. Take in the threshold for enhanced pay (35) as another parameter.  Set this parameter to default to 35 if unspecified.  So your existing test code does not require change.  Specifying a default parameter value is easy.  To specify a default for `enhancement_threshold` use somthing like...

`def basic_pay(rate_per_widget, quantity_made, enhancement_threshold = 35):
`

Get this working first.  THEN try it with a specified value for the enhanced payment

Similarly take in the second enhanced payment threshold (45) as a parameter, also give this one a default value


### Recursive function

Write the traditional recursive version of a function to calculate factorials.

Try implementing the same calculation as a NON-recursive function.
