# Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. 

tuple1 = (0,1,2,3,4) #(0, 1, 2, 3, 4)
tuple2 = ("a", "b", "c", "d") # ('a', 'b', 'c', 'd')
tuple3 = (tuple1, tuple2) # ((0, 1, 2, 3, 4), ('a', 'b', 'c', 'd'))
# print(tuple1)
# print(tuple2)
# print(tuple3)

# print(tuple2 * 3) # ('a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd')

tuple4 = tuple1 + tuple2
# print(tuple4) # (0, 1, 2, 3, 4, 'a', 'b', 'c', 'd')

fullName = ("Rwitesh", "Bera")
firsname, lastname = fullName
# print(firsname) # Rwitesh
# print(lastname) # Bera

print(fullName[0])
# fullName[1] = "Rwitesh" # You cannot modify tuple element, it is immutable
 