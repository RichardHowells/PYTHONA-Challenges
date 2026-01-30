## Lab01 - TDD

## Flush printing text

Newspapers and magazines often print lines such that the first character aligns on the left margin and the last character aligns on the right margin.  With a fixed pitch font this is done by adding extra spaces between the words to push the rightmost character to the correct position.

Clearly it looks silly to put (say) five spaces before the last word.  The (say) five spaces should be distributed, evenly as possible, into the gaps between the words on the line.  The process is a little more complex with variable pitch fonts, but the idea is the same

The lab doesn't implement the entire functionality, just a couple of useful parts. You can complete it later if you like!

1. Paste this code into a new file to make the test framework

    ```Python
    import unittest

    def add(a, b):
        return a + b

    class TestAddFunction(unittest.TestCase):
        def test_add_positive_numbers(self):
            self.assertEqual(add(1, 2), 3)

        def test_add_negative_numbers(self):
            self.assertEqual(add(-1, -2), -3)

        def test_add_mixed_numbers(self):
            self.assertEqual(add(1, -2), -1)
            self.assertEqual(add(-1, 2), 1)

    if __name__ == '__main__':
        unittest.main()
    ```

1. The short description of how it works...
    - the `if __name__ == '__main__':` is a handy Python trick.  It is un-enclosed code so it runs if the module is executed stand alone, it is also executed if the module is imported.  It relies on Python behaviour that when a module runs stand-alone the special variable `__name__` is set to the magic value `'__main__'`.  Therefore this is a condition that determines if the module is being run stand alone
    - If it **is** being run stand alone then we call the main function in the testing package
    - The testing package's `main` function then finds classes that inherit from `unittest.TestCase` and executes all those member functions with names beginning with `test_`

    - When imported to another module then the condition skips executing any of the tests

    - This trick is handy as it allows the tests to stay with the implementation code. They are more likley to be kept up to date and less likely to be lost

1. Start off by adding a test for a function that takes a string, (the text for the line), and an integer, (the intended length of the line).  
    - this function should return BOTH the words, as a list, and the number of spaces to fill the line to the desired length. Simplest is to return a tuple `return (wordsList, requiredSpaces)`.  The caller can then sequence unpack that result `words, spaces = f(...)`
    - assert that the list of words contains the expected words
    - assert that the calculated number of spaces is correct
    - Of course real life lines are maybe 80 characters long and have maybe ten plus words.  You should keep it simple, maybe three words.  Pick your own line length but it needs to be large enough for the words and the spaces...  Follow the pattern of the existing tests. Maybe
    ```Python
        def test_lineDecomposition(self):
            words, spaces = split_line_to_words_and_spaces("the..   boy", 12)
            self.assertEqual(words, ["the..",  "boy"])
            self.assertEqual(spaces, 4)
    ```

1. Run your file.  You expect it to crash because you have no function yet

1. Write the header line for your line splitting function, and implement it's functionality.  Keep running the tests until they pass

1. Once those tests pass for your split function...

1. Write a test for a function that takes a list of words, and a number (the number of spaces required to separate the words of the line AND pad it to the required length).  
    - You will notice that this is exactly what the previous function emits, but you should TEST THIS ONE INDEPENDANTLY
    - Your test might look like this
    ```Python
   
        def test_distributeExcessSpacesAtEndOfLine(self):
            line = distribute_spaces_at_end(["the..", "boy", "stood", "on"], 4)
            self.assertEqual(line, "the.. boy stood  on")
    ```
    - notice that there are three words, but a demand for four spaces.  That is why in the assertion there are TWO spaces between 'stood' and 'on' 

    - Now write the code to make this pass.

1. Add more cases, some ideas...
    - a line with one word
    - a five word line with, say, seven spaces required.  You decide what should happen.  Write the test, then make it pass
