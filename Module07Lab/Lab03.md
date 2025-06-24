## Lab03 File Handling


1. Write a program to read a text file (just hard code a file name) and display the contents using `print()`

    - Create some test data.  Suggestion... some imaginary, 5 digit, employee numbers

    - Test your program

1. Enhance your program so that it reads the input file.  But only displays an employee number on the first occasion it appears in the file

    - Suggestion, check each incoming employee number in a `set`.  
    - If it is NOT present in the set, `print` it and add it to the set.

1. Enhance your program to both print the output and write it to a new file (hard code the file name)

## Bonus ideas

1. Do a bit of research to find out how to access command line arguments
    - Allow the file names to be supplied at the command line.
    - For this you should run the program from a command prompt window.
    - On our VM's python is installed in a subdirectory `anaconda3`.  So from the standard `LabUser` directory you would run somthing like...
`.\anaconda3\python yourprogram.py inputFile outputFile`

1. Do a bit more research and give the user a warning if they are about to overwrite an existing file



