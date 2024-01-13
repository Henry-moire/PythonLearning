import re

# Your code goes here
find_members = []
for name in dir(re):
    if('find' in name):
        find_members.append(name)

print(sorted(find_members))