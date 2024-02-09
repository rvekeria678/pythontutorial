# Python JSON

# Source: https://www.w3schools.com/python/python_json.asp

# JSON -> JavaScript Object Notation
# syntax for storing and exchanging data

import json

# Converting JSON to Python
x = '{"name":"Larry", "age":62, "state":"WA"}'

y = json.loads(x)

print(y["age"])

# Converting Python to JSON
a = {
    "manufacturer": "honda",
    "model": "hrv",
    "horsepower":142
}

b = json.dumps(a)

print(b)

# The following types can be converted to JSON; their equivalent typs are shown on the left

# dict -> Object
# list -> Array
# tuple -> Array
# str -> String
# int -> Number
# float -> Number
# True -> true
# False -> false
# None -> null

# Formatting -> indenting/separators
c = json.dumps(a, indent = 4, separators=("."," = "))
print(c)

# Order
d = json.dumps(a, indent=4, sort_keys=True)
print(d)