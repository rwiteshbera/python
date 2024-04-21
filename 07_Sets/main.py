# A Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements. 
language = {"C++", "Java", "Python", "Go", "Java"}
# print(language) # Unordered # Can be printed in any order # No duplicate: It will not contain duplicate

language.add("Kotlin")
# print(language)

a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e', 'f'}
c = a.intersection(b)
d = a.union(b)
e = a.difference(b)
f = b.difference(a)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# Remove Item from a set
# print(a.pop()) # Remove a random element from the set and return that removed element
# print(a)

# a.remove('c') # Remove 'c' from set a
# print(a)


# Check if an element is present in a set
# data = {12, 21, 23, 18, 44, 23}
# print(21 in data) # True
# print(22 in data) # False