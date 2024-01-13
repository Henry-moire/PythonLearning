#Functions in python are defined using the block keyword "def", followed with the 
#function's name as the block's name. For example:
def my_function():
    print("Hello From My Function!")

#Functions may also receive arguments (variables passed from the caller to the function). For example:
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

#Functions may return a value to the caller, using the keyword- 'return' . For example:
def sum_two_numbers(a, b):
    return a + b

#To call a function simply write the name followed by (), placing any required arguments within the brackets
# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)