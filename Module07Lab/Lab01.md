## Lab01 Strings

### Fancy additional features in strings

1. Print this string:
    `s = "I am a two\nline string"`

    - notice that the \n is output as a newline character
    - in a 'simple' string the '\' character means "Here is somthing special", and the following character tells you what the special somthing is
        - \n == a new line
        - \t == a horizontal tab
        - \\ == nope!  I really did want a SINGLE backslash

1. Turn off the special '\' behaviour with a 'raw string' indicated with an r prefix
    - print this string
    - `s = r"My backslash is not special \n it's just part of the string`
    - notice that the \ and the n are just printed normally

1. Formatting output
    - there are a LOT of ways to do this
    - formatted strings have an f prefix and embed expressions to print
    - try this code
    ```
    name = "Richard"
    age = 21.5
    formatted_message = f"{name} is {age + 1} years old, next birthday."
    print(formatted_message)
    ```
    - as written this uses the default formatting rules for each expression.  Essentially, "Output in the minimum number of characters you can get away with"
    - you can control this with a format expression, after a colon.  Something like `{age + 1:5.2f}` which says "I want five chars of output with two digits after the decimal point".  Experiment with this type of format.