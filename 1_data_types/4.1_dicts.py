# dicts/dictionaries are roughly equivalent to hashmaps in other languages
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)

# to select the value of some key
print(my_dict['a'])

# you can also use the .get function to provide a default value if the key doesn't exist
print(my_dict.get('f', "my default value"))

# to set a value in the dict
my_dict['d'] = 4
print(my_dict)

# get all keys
print(my_dict.keys())

# get all values
print(my_dict.values())

# get all entries
print(my_dict.items())

# deleting an entry
del my_dict['a']
print(my_dict)

# dicts, like lists, can contain mixed types, but the key must be hashable
mixed_dict = {
    1: 'a', 
    'hello': 64.4, 
    63.3: [1,2,3], 
    'dict': {'a': 'b'}
    }