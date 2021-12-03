# declaring a list
my_list = ["Hello", "there", "!"]

# lists have lengths
print(len(my_list))

# lists can contain mixed types
my_mixed_list = ["Hello", 5.3, True, [1,2,3]]

# lists can be printed
print(my_list, my_mixed_list)

# lists can be appended to
my_list.append("?")
print(my_list)

# items can be removed by index
my_list_of_numbers = [1,2,3,4,5,6]
del my_list_of_numbers[1]
print(my_list_of_numbers)

# or by value
my_list_of_numbers = [1,2,3,4,5,6]
my_list_of_numbers.remove(1)
print(my_list_of_numbers)

# or using pop
my_list_of_numbers = [1,2,3,4,5,6]
my_list_of_numbers.pop()
print(my_list_of_numbers)

# checking if a value exists in a list
print("Hello" in my_list)

# lists can be deconstructed into variables
a, b, c = ["alpha", "beta", "gamma"]
print(c) # gamma

# unpacking can be used for variable length lists
a, b, *c = ["alpha", "beta", "gamma", "delta", "lambda", "epsilon"]
print(a) # alpha
print(c) # ["gamma", "delta", "lambda", "epsilon"]
