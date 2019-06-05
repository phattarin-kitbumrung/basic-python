#To open the file, use the built-in open() function.
#The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())


#By default the read() method returns the whole text, but you can also specify how many character you want to return:
#Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))


#By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)


#Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")


#Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")


#To delete a file, you must import the OS module, and run its os.remove() function:
import os
if os.path.exists("demo2.txt"):
  os.remove("demo2.txt")
else:
  print("The file does not exist")