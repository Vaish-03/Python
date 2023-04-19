#variables = it is container in which we put a values.
#Variables do not need to be declared with any particular type
x = 5 #int
y = "Vaish" #str
print(x)
print(y)

#casting
x = int(5)
y = str("5")
z = float(5)
print(x)
print(y)
print(z)

#data type of a variable with the type() function
x = 5
y = "Vaish"
print(type(x))
print(type(y))

#Variable names are case-sensitive.
age = 5
AGE = 6
print(age)
print(AGE)

#A variable name cannot start with a number
#2myvar = "John" # error

#A variable name must start with a letter or the underscore character
_myvar = 5
myvar = "Vaish"
print(_myvar)
print(myvar)

#assign values to multiple variables in one line
a,b,c = "blue","red","yellow"
print(a)
print(b)
print(c)

#Same values to multiple variables on single
x=y=z = "Pink"
print(x)
print(y)
print(z)

#collection of values in a list, tuple etc
# Python allows to extract the values into variables.
colours = ["Red","Pink","Blue"]
a,b,c = colours
print(a)
print(b)
print(c)

#Variables that are created outside of a function => global variable(used by outside and inside)
x = "account"
def myfun():
    print("It is my new " + x)
myfun()

#to create golabal variables inside the fun use 'global' keyword
def myfunc():
  global x
  x = "accouhnt"

myfunc()

print("It is my new " + x)





