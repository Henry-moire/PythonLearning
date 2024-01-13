# How to define an integer
myint = 7
print(myint)
# How to define a floatong point number
myfloat = 7.1
print(myfloat)
# How to define a string
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
# The difference between the two is that using double quotes makes it easy to 
# include apostrophes (whereas these would terminate the string if using single quotes)
mystring = "Don't worry about apostrophes"
print(mystring)
# Simple operations can be executed on numbers and strings
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + "" + world
print(helloworld)

# Assingments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4
print(a, b)

# Mixing operations between numbers and strings is not supported
# This will not work!
#one = 1
#two = 2
#hello = "hello"
#print(one + two + hello)