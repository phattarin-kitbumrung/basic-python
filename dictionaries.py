#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
mydict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)

#Get the value of the "model" key:
x = mydict["model"]
x = mydict.get("model")
print(x)

#You can loop through a dictionary by using a for loop.
#Print all key names in the dictionary, one by one:
for x in mydict:
  print(x)
#Print all values in the dictionary, one by one:
for x in mydict:
  print(mydict[x])
#Loop through both keys and values, by using the items() function:
for x, y in mydict.items():
  print(x, y)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
mydict["color"] = "red"
print(mydict)

#There are several methods to remove items from a dictionary:
#The pop() method removes the item with the specified key name:
mydict.pop("model")
print(mydict)
#The del keyword removes the item with the specified key name:
del mydict["year"]
print(mydict)