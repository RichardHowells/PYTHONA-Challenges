

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