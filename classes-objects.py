#To create a class, use the keyword class:
class MyClass:
  x = 5

#Now we can use the class named myClass to create objects:
p1 = MyClass()
print(p1.x)

#Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

#You can modify properties on objects like this:
p1.age = 40
#You can delete properties on objects by using the del keyword:
del p1.age
#You can delete objects by using the del keyword:
del p1