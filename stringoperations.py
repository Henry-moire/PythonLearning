astring = "Hello world!"
print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7]) #This prints a slice of the string, starting at index 3, and ending at index 6.
#If you just have one number in the brackets, it will give you the single character at that index. 
#If you leave out the first number but keep the colon, it will give you a slice from the start to 
#the number you left in. If you leave out the second number, it will give you a slice from the first 
#number to the end.
#You can even put negative numbers inside the brackets. They are an easy way of starting at the end 
#of the string instead of the beginning. This way, -3 means "3rd character from the end".

print(astring[3:7:2]) #This prints the characters of string from 3 to 7 skipping two character. 
#This is extended slice syntax. The general form is [start:stop:step].

#There is no function like strrev in C to reverse a string. But with the above mentioned type of 
#slice syntax you can easily reverse a string like this
print(astring[::-1])

#These make a new string with all letters converted to uppercase and lowercase, respectively.
print(astring.upper())
print(astring.lower())

#This is used to determine whether the string starts with something or ends with something, respectively.
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

#This splits the string into a bunch of strings grouped together in a list. Since this example splits 
#at a space, the first item in the list will be "Hello", and the second will be "world!".
afewwords = astring.split(" ")