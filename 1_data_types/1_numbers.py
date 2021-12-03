# declaring constants
PI = 3.141592653

# declaring variables
diameter = 25.3
circumference = diameter * PI

# numbers
a = 26          # int
b = 84.2        # float
c = -74e2       # scientific notation
d = 0x74        # hexadecimal
e = 0o44        # octal
f = 0b1010      # binary
g = 100_000     # underscores are valid

# different number types generally don't need to be casted to interoperate
print(a+b+c+d+e+f+g)

# division returns floats by default, but integer divison also exists
print(4/2)      # 2.0
print(3.0/2.0)  # 1.5
print(3/2)      # 1.5
print(3//2)     # 1
