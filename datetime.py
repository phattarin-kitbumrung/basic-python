import datetime

#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))


#To create a date, we can use the datetime() class (constructor) of the datetime module.
x = datetime.datetime(2020, 5, 17)
print(x)
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))