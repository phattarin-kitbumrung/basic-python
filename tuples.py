#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
mytuple = ("apple", "banana", "cherry")
print(mytuple)

#Once a tuple is created, you cannot change its values. Tuples are unchangeable.
#mytuple[1] = "blackcurrant" # This will raise an error
#print(mytuple)

#You can loop through the tuple items by using a for loop.
for x in mytuple:
  print(x)

#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#mytuple[3] = "orange" # This will raise an error
#print(mytuple)

#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
#del mytuple
#print(mytuple) #this will raise an error because the tuple no longer exists
