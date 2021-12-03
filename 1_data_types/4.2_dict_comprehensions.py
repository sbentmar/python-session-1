# dict comprehensions are similar to list comprehensions, but instead used to create dicts
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 100, 'e': 3, 'f': 68.2}

# filter out all values below 20
no_values_below_20 = {k:v for k,v in my_dict.items() if v >= 20}
print(no_values_below_20)

# add 'hello' to all keys
hello_keys = {'hello'+k:v for k,v in my_dict.items()}
print(hello_keys)

# multiply all values by 5
values_multiplied_by_five = {k:v*5 for k,v in my_dict.items()}
print(values_multiplied_by_five)

# and everything combined to one
all_in_one = {'hello'+k:v*5 for k,v in my_dict.items() if v >= 20}
print(all_in_one)

# it's also simple to convert e.g. a list into a dict
# mapping "id" to key and "size" to value
my_list = [
    {'id': 69, 'size': 25}, 
    {'id': 86, 'size': 36}, 
    {'id': 53, 'size': 97}, 
    {'id': 97, 'size': 236}, 
    {'id': 235, 'size': 6845}
]

list_as_dict = {item['id']:item['size'] for item in my_list}
print(list_as_dict) # {69: 25, 86: 36, 53: 97, 97: 236, 235: 6845}