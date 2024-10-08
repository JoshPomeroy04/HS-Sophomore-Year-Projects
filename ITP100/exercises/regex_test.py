import re

start = open('data.txt', 'r')
for items in start:
    if re.search('b', items):
        print(items)
