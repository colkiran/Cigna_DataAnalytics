"""
Reading JSON Data
load - used to read the json document from a file
loads - used to convert JSON string to python dictionary
"""

import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

# print(jsonFile)
for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print('-' * 60)

JFR.close()

print('loads'.center(60, "-"))
# data should be enclosed in single quotes
empdata = '{"name": "mike", "age": 29, "city": "Melbourne"}'
print(empdata)
print(type(empdata))

print('-' * 60)
# convert the string into python dictionary
res = json.loads(empdata)
print(res)
print(type(res))
for k, v in res.items():
    print(k, "=>", v)
