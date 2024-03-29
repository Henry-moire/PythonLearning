#A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
#Each value stored in a dictionary can be accessed using a key, which is any type of 
#object (a string, a number, a list, etc.) instead of using its index to address it.
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
#or
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#Iterating over dictionaries
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#Removing a value
del phonebook["John"]
#or
phonebook.pop("John")