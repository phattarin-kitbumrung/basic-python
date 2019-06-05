#A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
mylist = ["apple", "banana", "cherry"]
print(mylist)

#To change the value of a specific item, refer to the index number:
mylist[1] = "blackcurrant"
print(mylist)

#You can loop through the list items by using a for loop:
for x in mylist:
 print(x)

#The del keyword removes the specified index:
del mylist[0]
print(mylist)

#add an item at the specified index, use the insert() method:
mylist.insert(0, "apple")
print(mylist)

