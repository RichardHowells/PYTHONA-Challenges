

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