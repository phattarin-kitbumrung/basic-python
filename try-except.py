#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


#Try to open and write to a file that is not writable:
f = open("demofile.txt")
try:
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()