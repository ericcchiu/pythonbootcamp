print("hello world")
print(len("hello"))

# Indexing and slicing with strings
mystring = "Hello World"
print(mystring)
print(mystring[0])
print(mystring[-2])

mystring1 = 'abcdefghijklmn'
print(mystring1[2:])  # cdefghijklmn everything after c
print(mystring1[:3])  # abc up to c
print(mystring1[1:6])  # bcdef
print(mystring1[::3])  # adgjm
print(mystring1[::-1])  # reverses a string
print('tinker'[1:4])  # ink

# String properties and methods
# Immutability
name = 'Sam'
last_letters = name[1:]
print(last_letters)

print('It is 9 ' + last_letters)
print(last_letters * 20)

print(name.upper())
print(name.split())
