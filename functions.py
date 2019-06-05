#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Return Values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#Recursion
def myrecursion(k):
  if(k>0):
    result = k+myrecursion(k-1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
myrecursion(6)