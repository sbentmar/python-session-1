# list comprehensions can perform tasks similar to map/filter functions
numbers = list(range(0,10))

# filter out all numbers below 5
numbers_below_5 = [n for n in numbers if n < 5]
print(numbers_below_5)

# this is equivalent to the following use of filter
numbers_below_5 = list(filter(lambda n: n < 5, numbers))
print(numbers_below_5)

# multiplying all numbers by 5
numbers_times_5 = [n*5 for n in numbers]
print(numbers_times_5)

# this is equivalent to the following use of map
numbers_times_5 = list(map(lambda n: n*5, numbers))
print(numbers_times_5)

# list comprehensions can combine map and filter in a single operation
numbers_under_5_times_5 = [n*5 for n in numbers if n < 5]
print(numbers_under_5_times_5)

# which is equivalent to the following use of map/filter
print(list(map(lambda n: n*5, filter(lambda n: n < 5, numbers))))
