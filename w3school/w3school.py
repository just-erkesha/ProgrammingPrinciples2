#1exercise
print("Hello, World!")

#2exercise
if 5 > 2:
 print("Five is greater than two!") 

#3exercise
# "comment"

#4exercise
"""
Multiline comments
"""

#5exercise
carname="Volvo"

#6
x=50

#7
x=5
y=10
print(x+y)

#8
x=5
y=10
z=x+y
print(z)

#9
#2my-first_name = "John"
my_first_name = "John"

#10
x=y=z="Orange"

#11
def myfunc():
 global x
 x="fantastic"

#12  int
x=5
print(type(x))

#13   str
print(type("Hello World!"))

#14  float
print(type(20.5))

#15  list
x= ["apple", "banana", "cherry"]
print(type(x))

#16  tuple
x= ("apple", "banana", "cherry")
print(type(x))

#17  dict
x = {"name" : "John", "age" : 36}
print(type(x))

#18  bool
x = True
print(type(x))

#19
x = 5
x = float(x)

#20
x = 5.5
x = int(x)

#21
x = 5
x = complex(x)

#22
x = "Hello World"
print(
len(x)
)

#23
txt = "Hello World"
x = txt[0]

#24
txt = "Hello World"
x = txt[2:5]

#25
txt = " Hello World "
x = txt.strip()

#26
txt = "Hello World"
txt = txt.upper()

#27
txt = "Hello World"
txt = txt.lower()

#28
txt = "Hello World"
txt = txt.replace("H","J")

#29
age = 36
txt = "My name is John, and I am 36"
print(txt.format(age))

#30  True
print(10 > 9)

#31  False
print(10 == 9)

#32  False
print(10 < 9)

#33  True
print(bool("abc"))

#34  False
print(bool(0))

#35
print(10 * 5)

#36
print(10/2)

#37
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#38
if 5!=10: 
  print("5 and 10 is not equal")

#39
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#40
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#41
fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"

#42
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#43
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#44
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#45
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#46
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#47
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#48
fruits = ("apple", "banana", "cherry")
print( fruits[0])

#49
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#50
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#51
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#52
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#53
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#54
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#55
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#56
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#57
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#58
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020

#59
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"


#60
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")


#61
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#62
a = 50
b = 10
if a>b:
 print("Hello World")

#63
a = 50
b = 10
if a!=b:
 print("Hello World")

#64
a = 50
b = 10
if a ==b:
  print("Yes")
else:
  print("No")

#65
a = 50
b = 10
if a ==b:
  print("1")
elif a >b:
  print("2")
else:
  print("3")

#66
if a == b  and  c == d:
  print("Hello")

#67
if a == b  or  c == d:
  print("Hello")

#68
if 5 > 2:
  print("Five is greater than two!")

#69
if 5 > 2: print("Five is greater than two!")

#70
print("Yes") if 5 > 2 else print("No")

#71
i = 1
while i < 6:
  print(i)

#72
i = 1
while i < 6:
  if i == 3:  
    break
  i += 1

#73
i = 1
while i < 6:
  if i == 3:  
    continue
  i += 1

#74
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#75
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#76
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#77
for x in range(6):
  print(x)

#78
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":  
    break
  print(x)

#79
def my_function():
  print("Hello from a function")

#80
def my_function():
  print("Hello from a function")
my_function()

#81
def my_function(fname, lname):
  print(fname)

#82
def my_function(x):
 return x + 5


#83
def my_function(*kids):
  print("The youngest child is " + kids[2])

#84
def my_function(**kid):
  print("His last name is " + kid["lname"])

#85
x = lambda a : a

#86
class MyClass:
  x = 5

#87 
class MyClass:
  x = 5
p1 = MyClass()



#88
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

#89
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#90
class Student(Person):

#91
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()


#92
import mymodule

#93
import mymodule as mx

#94
import mymodule
print(dir(mymodule))

#95
from mymodule import person1