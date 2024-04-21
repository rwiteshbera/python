# A String is a data structure in Python that represents a sequence of characters. It is an immutable data type, meaning that once you have created a string, you cannot change it. 
name = "Rwitesh"
# print(name)

# Access character
# print(name[0]) # 0tu index
# print(name[1]) # 1st index
# print(name[-1]) # Last index
# print(name[-2]) # second last index


fullName = "Rwitesh Bera"
# print(fullName[2:5]) # Slice [Index 2 - 4] # Last index is exclusive
# print(fullName[:8]) # [Index 0 - 7]
# print(fullName[2:]) # [Index 2 - end]
# print(fullName[2:-2]) # [Index 2 - 2nd last character]

# Reverse a string
# print(fullName[::-1])

# Deleting a character
# print(fullName)
# del fullName[1] # Not possible # String is immutable
# print(fullName)

# print(fullName)
# print(fullName[0:1] + fullName[2:])


# Delete entire string
# a = "Character A"
# print(a)
# del a
# print(a) # 'a' is not defined

# Convert Uppercase -> Lowercase
# Lowercase -> Uppercase
b = "Value Investing"
# print(b.swapcase()) # vALUE iNVESTING
# print(b.endswith("g")) # Return True if ends with 'g'
# print(b.startswith("b")) 
# data = b.replace("Investing", "Investment") # Replace old string with new one
# print(data)

# Check string length
print(len(b))