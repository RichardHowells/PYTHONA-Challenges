
print("build the message as a string")

for i in range(0,21):
    message = ''

    if i % 3 == 0:
        message += "Fizz "

    if i % 5 == 0:
        message += "Buzz "

    if message != "":
        print(message)
    else:
        print(i)

print("Use print's ability to remain on the current line")
for i in range(0,21):
    if i % 3 == 0:
        print("Fizz ", end="")

    if i % 5 == 0:
        print("Buzz ", end="")
    
    # With this technique the modulus tests are repeated because
    # we have to decide if the print line is completed
    # It's a risk to have repeated code
    if i % 3 == 0 or i % 5 == 0:
        print("")
    else:
        print(i)

# As a manually coded loop
i = 0
while i < 21:
    message = ''

    if i % 3 == 0:
        message += "Fizz "

    if i % 5 == 0:
        message += "Buzz "

    if message != "":
        print(message)
    else:
        print(i)
    i += 1



# For the bonus parts
upper_limit = int(input("Please enter an upper limit "))
for i in range(upper_limit):
    message = ''

    if i % 3 == 0:
        message += "Fizz "

    if i % 5 == 0:
        message += "Buzz "

    # For the bonus part
    if i % 7 == 0:
        message += "Whoosh "

    if message != "":
        print(message)
    else:
        print(i)