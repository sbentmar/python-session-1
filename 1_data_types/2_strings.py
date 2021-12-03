# declaring a string
BASIC_GREETING = "hello there"

# string concatenation
my_greeting = BASIC_GREETING+"!"
print(my_greeting)

# strings are UTF-8 by default
russian_hello = "привет!"
print(russian_hello)

# there are different kinds of strings

#binary strings are arrays of bytes
binary_string = b"I'm an ASCII string!"
print(binary_string)

# russian_binary_string = b"привет!" <- will not work!
# binary representation would instead be:
russian_hello_binary = russian_hello.encode()
print(russian_hello_binary)

# raw strings have no interpolation, useful for e.g. regex
import re
dog_test = "I am a dog"
cat_test = "I am a cat"
hat_test = "I am a hat"
pattern = r".*\s(cat|dog)$"
print(re.search(pattern, dog_test))
print(re.search(pattern, cat_test))
print(re.search(pattern, hat_test))

# f strings add more string interpolation
f_string = f"{my_greeting} {dog_test}. I am {15+63-33*0.5} years old!"
print(f_string)
