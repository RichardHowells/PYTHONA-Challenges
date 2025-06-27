import os

# We use relative paths in this code.  
# Before getting going let's just confirm the current working directory 
print(os.getcwd())

print("All lines in the file\n")

file = open(r"Module07Lab\employees.txt")
for line in file:
    print(line.strip())

file.close()

print("\nJust the unique ones\n")
# Display only unique items
file = open(r"Module07Lab\employees.txt")

import pathlib 
my_file = pathlib.Path(r"Module07Lab\unique_employees.txt")
if my_file.is_file():
    print("I am about to nuke your file")


output_file = open(r"Module07Lab\unique_employees.txt", "w")
emp_nos = set()
for line in file:
    if not line in emp_nos:
        emp_nos.add(line)
        print(line.strip())
        output_file.write(line)

file.close()