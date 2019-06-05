#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
myset = {"apple", "banana", "cherry"}
print(myset)

#You can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in myset:
  print(x)

#To add one item to a set use the add() method.
myset.add("orange")
print(myset)
#Add multiple items to a set, using the update() method:
myset.update(["orange", "mango", "grapes"])
print(myset)

#Remove "banana" by using the remove() method:
myset.remove("banana")
print(myset)
#Remove "orange" by using the discard() method:
myset.discard("orange")
print(myset)

#Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print(z)

#Return a set that contains the items that exist in both set x, and set y:
z = x.intersection(y) 
print(z)

#Return a set that contains all items from both sets, duplicates are excluded:
z = x.union(y) 
print(z)