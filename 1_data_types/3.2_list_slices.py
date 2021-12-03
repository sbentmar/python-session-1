# generate a list with values from 0 to 29
long_list = list(range(0,30))

# slices can be used to operate on parts of lists
# select the first element
print(long_list[0])

# select elements 10-20
print(long_list[10:20])

# select the 10th element from the end
print(long_list[-10])

# select the last 10 elements in the list
print(long_list[-10:])

# select the elements between the 10th and the 5th element from the end
print(long_list[-10:-5])

# setting step size
# select every second element between 10 and 20
print(long_list[10:20:2])

# step backwards through list (i.e. reverse it)
print(long_list[::-1])

# select every other elements between the 10th and the 5th element from the end
print(long_list[-10:-5:2])

# select every other element, going backwards
print(long_list[-1:0:-2])

# assigning to slices
# replace the first 5 values with other values
long_list[0:5] = [0,0,0,0,0]
print(long_list)

# deleting the last 5 values
del long_list[-5:]
print(long_list)

# strings are represented as lists internally, so any functions that work on lists also work on strings (generally)
print(sorted(my_greeting))
print(len(my_greeting))

# this is also used to extract substrings
# extract the first letter
print(my_greeting[0])
# extract the first three letters
print(my_greeting[0:3])
# extract every second letter in the first 10 letters
print(my_greeting[0:10:2])

# check if string contains "the"
print("the" in my_greeting)
