# tuples are very similar to lists, but are immutable
a = (1, 2, 3)
print(a[1])

# a[1] = 16   # does not work!
# del a[1]    # does not work!

# tuples are hashable (if the items are), so they can be used as keys in dicts
my_tuple_dict = {
    (1,2): "something",
    (7,3): "hello",
    (9,22): "another thing"
 }
print(my_tuple_dict)


# the same is not true for lists, so this will not work
my_list_dict = {
    [1,2]: "something",
    [7,3]: "hello",
    [9,22]: "another thing"
 }
print(my_list_dict)
