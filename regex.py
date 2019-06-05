import re

#Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")


#The findall() function returns a list containing all matches.
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
#Return an empty list if no match was found:
str = "The rain in Spain"
x = re.findall("Portugal", str)
print(x)


#Search for the first white-space character in the string:
str = "The rain in Spain"
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start())
#If no matches are found, the value None is returned:
str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)


#The split() function returns a list where the string has been split at each match:
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
#Split the string only at the first occurrence:
str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)


#The sub() function replaces the matches with the text of your choice:
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)
#You can control the number of replacements by specifying the count parameter:
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)


#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S":
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())
#Print the string passed into the function:
print(x.string)
#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S":
print(x.group())