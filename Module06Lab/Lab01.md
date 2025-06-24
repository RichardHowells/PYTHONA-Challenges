## Lab01 Sequences

There are two major ways of using sequences, homogenous and hetrogenous

A homogenous sequence has data items all of the same type.  In any other languages the corresponding type is an array.  Example:
prime_numbers = (1, 3, 5, 7, 11, 13)

A hetrogeneous sequence contains a data items of different type (or different business meaning).  Example:
employee = (1011, "Bob", "Harris", "Programmer", 2001-05-01, 30000) - here the language has no way to help the programmer determine the business meaning.  At a guess 1011 might be employee number, 2010-05-01 might be a start date, or a date of birth.  Classes are more descriptive for this kind of data.


1. Create a tuple containing the integer numbers from 1 to 20

1. Print the first number, print the last number

1. Use slicing to pick off the first 10 numbers, and the last 10

1. Use a step to pick out all the even subscripted items ie [2], [4], [6], etc

1. Use a step to pick out all the odd subscripted items ie [1], [3], [5], etc

1. Set up this string...
    - `text = "The boy stood on the burning deck Whence all but he had fled"
    - use `string.split()` to separate the words into individual entries in a list

    - Use the `input` function to have the user enter a word.  Display "Yes" if the user's word is present in the string.  HINT use the `in` operator to determine if an entry is present in the list

    - modify your code such that the test is case IN-sensitive.  Ie if the user enters Whence, wHence, or WHENCE the program should report Yes for EACH of them
    