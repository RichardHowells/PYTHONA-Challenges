"""
Docstring for Module06Lab.Lab01-Solution

This is a sample code from the python course
"""



numbers = tuple(range(1, 21))

print(numbers)

print(numbers[0], numbers[-1])


first_ten = numbers[:10]
last_ten = numbers[10:]

print(first_ten, last_ten)

evens = numbers[0::2]
odds = numbers[1::2]
print(evens, odds)



text = "The boy stood on the burning deck Whence all but he had fled"

# To make case insensitive...
text = text.lower()

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

# Count word occurrences

wordlist = ["the", "cat", "sat", "sat", "sat", "on", "the", "mat"]

wordCounts = dict()
for word in wordlist:
    if word in wordCounts:
        wordCounts[word] = wordCounts[word] + 1
    else:
        wordCounts[word] = 1

print(wordCounts)

wordCounts = dict()
for word in wordlist:
    count = wordCounts.get(word, 0)
    wordCounts[word] = count + 1

print(wordCounts)

import collections

wordCounts = collections.Counter(wordlist)

print(wordCounts)