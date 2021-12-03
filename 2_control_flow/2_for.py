# for loops in python are more like foreach loops in other languages

names = ["Wally", "Molly", "Polly"]

for name in names:
    print(name)

# if you want indicies, you need to enumerate your lists
for idx, name in enumerate(names):
    print(idx, name)

# to loop over a range of numbers, the range object is used:
for n in range(0,5):
    print(n)

# you can use break in continue in loops, like in other languages
for name in names:
    if name == "Wally":
        print("Found Wally!")
        break

# you can also attach an "else" to the loop, if you want to do something after reaching the end of the list 
for name in names:
    if name == "Wally":
        print("Found Wally!")
        break
else:
    print("Wally was not found in the list")
