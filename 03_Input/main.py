# value = input("Hello, What is your name? ") # Taking string input by default
# print(value)
# print(type(value))

# Integer Input
# age = int(input("Ente age: "))
# print(age)
# print(type(age))

# Float
# percentage = float(input("Enter percentage: "))
# print(percentage)
# print(type(percentage))

# Multiple Input at a time
# a, b, c = input("Enter three values: ").split()
# print(f"type = {type(a)} | a = {a}")
# print(f"type = {type(b)} | b = {b}")
# print(f"type = {type(c)} | c = {c}")

# Typecasting to int after taking multiple input a time
a, b, c = list(map(int, input("Enter three values: ").split()))
print(f"type = {type(a)} | a = {a}")
print(f"type = {type(b)} | b = {b}")
print(f"type = {type(c)} | c = {c}")