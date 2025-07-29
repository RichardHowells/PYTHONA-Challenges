numbers = tuple(range(1, 21))

print(numbers)

print(numbers[0], numbers[-1])


first_ten = numbers[:10]
last_ten = numbers[10:]

print(first_ten, last_ten)

evens = numbers[1::2]
odds = numbers[0::2]
print(evens, odds)



text = "The boy stood on the burning deck Whence all but he had fled"

# To make case insensitive...
#text = text.lower()

textWords = text.split(" ")

# Bonus - Convert the list into a set...
#textWords = set(textWords)
print(textWords)

desired = input("Give me a word :")

#To make case insensitive...
#desired = desired.lower()

if desired in textWords:
    print("Yes")
else:
    print("No")


