import json

#Convert from JSON to Python
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["name"])


#Convert from Python to JSON
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)


#Convert a Python object containing all the legal data types:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
#Use the indent parameter to define the numbers of indents:
#Use the separators parameter change the default separator:
y = json.dumps(x, indent=4, separators=(". ", " = "))
#Use the sort_keys parameter to specify if the result should be sorted or not:
z = json.dumps(x, indent=4, sort_keys=True)
print(y)
print(z)