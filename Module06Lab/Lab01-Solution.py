numbers = tuple((n for n in range(21)))
print(numbers)

print(numbers[0], numbers[-1])


first_ten = numbers[:10]
last_ten = numbers[10:]

print(first_ten, last_ten)

evens = numbers[::2]
odds = numbers[1::2]
print(evens, odds)



text = "The boy stood on the burning deck Whence all but he had fled"

#To make case insensitive...
text = text.lower()

print(text.split(" "))

desired = input("Give me a word :")

desired = desired.lower()

if desired in text:
    print("Yes")
else:
    print("No")
