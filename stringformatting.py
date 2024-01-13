#Python uses C-style string formatting to create new, formatted strings. 
#The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
#together with a format string, which contains normal text together with "argument specifiers", 
#special symbols like "%s" and "%d".

# Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

name = "John"
print("Hello, %s!" % name)
# To use two or more argument specifiers, use a tuple (parentheses):
name = "John"
age = 23
print("%s is %d years old." % (name, age))
#Any object which is not a string can be formatted using the %s operator as well. 
#The string which returns from the "repr" method of that object is formatted as the string. For example:
mylist = [1,2,3]
print("A list: %s" % mylist)