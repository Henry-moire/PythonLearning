#Basic class template:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
#to assign the above class(template) to an object you would do the following:
myobjectx = MyClass()
#Accessing Object Variables
print(myobjectx.variable)
#You can create multiple different objects that are of the same class(have the same 
#variables and functions defined).
myobjecty = MyClass()
myobjecty.variable = "yackity"
print(myobjecty.variable)
#Accessing Object Functions
myobjectx.function()

#init()
#The __init__() function, is a special function that is called when the class is being initiated. 
#It's used for assigning values in a class.
class NumberHolder:

   def __init__(self, number):
       self.number = number