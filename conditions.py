#Python uses boolean logic to evaluate conditions.

#Boolean operators 'and'  and 'or'
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

#The "in" operator could be used to check if a specified object exists within an iterable 
#object container, such as a list:
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#Python uses indentation to define code blocks, instead of brackets.
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

#A statement is evaulated as true if one of the following is correct:
#1. The "True" boolean variable is given, or calculated using an expression, such as an 
#arithmetic comparison.
#2. An object which is not considered "empty" is passed.

#Unlike the double equals operator "==", the "is" operator does not match the values of 
#the variables, but the instances themselves. For example:
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#Using "not" before a boolean expression inverts it:
print(not False) # Prints out True
print((not False) == (False)) # Prints out False