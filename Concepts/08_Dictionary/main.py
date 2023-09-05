# Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

data = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}
# print(data) # {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}
# print(data.get(1)) # One
# print(data.get(2)) # Two

# Remove last inserted key-value
data.popitem()
# print(data) # {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
# print(data.keys()) # dict_keys([1, 2, 3, 4])
# print(data.items()) # dict_items([(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')])

odd = {1: "One", 3: "Three", 5: "Five", 7: "Seven"}
even = {2: "Two", 4: "Four", 6: "Six", 8: "Eight"}

# in-place merge (|) operator
odd |= even

print(odd) # {1: 'One', 3: 'Three', 5: 'Five', 7: 'Seven', 2: 'Two', 4: 'Four', 6: 'Six', 8: 'Eight'}