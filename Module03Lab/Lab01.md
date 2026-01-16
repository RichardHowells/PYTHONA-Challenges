## Lab01 - Flow of control

### Fizz Buzz

There is a popular children's game Fizz Buzz.  The concept is easy a group of kids take turns to count ascending numbers... 1, 2, 3, 4, etc.  The twist is that every multiple of three is replaced by the word 'Fizz' and every multiple of five is replaced by the word 'Buzz'.  A multiple of both is replaced by 'Fizz Buzz'

So 1, 2, Fizz, 4, Buzz, Fizz... 8, Fizz, Fizz Buzz, 11...

1. Write a program to generate the correct results for numbers up to 20 (that's about as many as can fit on a screen)

You will want a loop to generate the basic numbers.  Create versions
- using `while` for the loop
- using `for` and `range` for the loop

Inside the loop you will want `if` statements to determine when to output the words fizz/buzz/fizzbuzz.  You also want a way to test the division.  The % operator will give the remainder after an integer division.  Try versions with
- three independent `if` statements
- a cascade of `if`/`else` statements


### Bonus ideas

Use the `input` function to allow the user to specify the upper limit of numbers

Try extending these different versions to emit 'whoosh' for mutiples of 7.  Bear in mind that requires support for Fizz/whoosh, buzz/whoosh, and fizz/buzz/whoosh as possible outputs.
