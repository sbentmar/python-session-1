# if statements work similarly to other languages

a = True
b = False

if a and b:
    print("A and B are both true")
elif a and not b:
    print("A is true, B is not")
else:
    print("something else happened")

# note that:
# * you don't need parantheses around your condition
# * the whitespace is mandatory, but you can also write one-liners using if:
if a: print("A is true!")

# if is also used instead of the ternary operator:
name = "Guppy"
age = 28
potentially_redacted_name = name if age > 18 else "REDACTED"
print(potentially_redacted_name) # Guppy

age = 17
potentially_redacted_name = name if age > 18 else "REDACTED"
print(potentially_redacted_name) # REDACTED