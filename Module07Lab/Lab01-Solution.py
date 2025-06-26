
s = "abc\ndef"
print(s)

s = "abc\\def"
print(s)

s = r"abc\n\def"
print(s)




name = "Richard"
age = 21.5
formatted_message = f"{name} is {age + 1} years old, next birthday."
print(formatted_message)

print(f"{name} is {age + 1:10.2f} years old, next birthday.")

