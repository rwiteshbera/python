# Create a list of numbers with given range
# Input : 5, 9
# Output : [5,6,7,8,9]

# def CreateList(left, right):
#     result = []
#     while(left <= right):
#         result.append(left)
#         left += 1
#     return result

# print(CreateList(5,9))
# print(CreateList(-5,9))


# Alternatve Way
left = 5
right = 12
list1 = list(range(left, right + 1))
print(list1)
