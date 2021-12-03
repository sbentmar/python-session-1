# while loops in python are very similar to other languages

i = 15

while i > 10:
    i -= 1
    print(f"i is now: {i}")

# like the for loop, it can also have an else clause:

i = 15
while i > 10:
    i -= 1
    print(f"i is now: {i}")
    if i == 13:
        break
else:
    print("i > 10 is no longer true")
