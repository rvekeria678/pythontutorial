# Python Dictionaries

# Source: https://www.w3schools.com/python/python_dictionaries.asp

# Dictionaries are used to store values in key-value pairs

# A Dictionary is a collection of ordered, changeable elements with no duplicates

my_dict = {
    "title": "Harry Potter and the Goblet of Fire",
    "author": "JK Rowling",
    "year":"2000"
}

# Ordered indicates that there is a defined order that will never change
# They are Changeable in that elements can be added, removed, or altered

# The following will ignore duplicates, only allowing accepting the last duplicate
my_dict2 = {
  "model": "F1215B(183)",
  "country": "United Kingdom",
  "caliber": 120,
  "caliber": 183
}

print(my_dict2)

# In Python, dictionaries are defined as objects with datatype of "dict":
print(type(my_dict2))

# The constructor for dict can also be accessed to create a new instance
my_dict3 = dict(name="Gary", age=45, country = "New Zealand")
print(my_dict3)