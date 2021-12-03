# declaring a function in python is done using the "def" keyword

def say_hello():
    print("Hello!")

# arguments work like you'd expect from other languages
def say_hello_with_name(name):
    print(f"Hello, {name}!")

# arguments can be optional
def say_hello_with_default(name = "Guppy"):
    print(f"Hello, {name}!")

# arguments can be typed
def say_hello_with_type(name: str):
    print(f"Hello, {name}!")

# as can return values
def get_hello_with_type(name: str) -> str:
    return f"Hello, {name}!"

# arguments can be unpacked to allow for variable sized arguments
def say_hello_to_many(*names):
    print(f"Hello, {' and '.join(names)}")

say_hello_to_many("Guppy", "Billy")

# functions can be stored in variables
a = say_hello_with_name
a("Sally")

# and in lists, dicts, tuples etc
my_function_dict = {
    "hello": say_hello_with_name
}
my_function_dict["hello"]("Billy")

# functions can be defined inside other functions, which will make them only visible inside that function (i.e. a closure)
def sort_by_id(people):
    def compare_id(person):
        return person["id"]
    people_copy = people.copy()
    people_copy.sort(key=compare_id)
    return people_copy

# you can also use lambdas to create anonymous functions, but these can only consist of a single expression (i.e. a single line)
def sort_by_id_lambda(people):
    people_copy = people.copy()
    people_copy.sort(key=lambda person: person["id"])
    return people_copy

my_list_of_people = [
            {"name": "Billy", "id": 100},
            {"name": "Willy", "id": 150},
            {"name": "Harry", "id": 50},
        ]


print(sort_by_id(my_list_of_people))
print(sort_by_id_lambda(my_list_of_people))
