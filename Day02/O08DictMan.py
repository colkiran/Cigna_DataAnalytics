
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'age': 34, 'runs': 120, 'oppn': 'WI'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'Rahul'), ('age', 31), ('runs', 65), ('oppn', 'SA')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='sourav', age=34, runs=80, oppn='Aus')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# print(dir(d1))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# fromkeys - to convert a list into a dictionary
# get - d2['nme'] => d2.get('nme', 'invalid key')
# items - combination of keys and values function - returns both key and value from a dictionary
# keys - will return all the keys from the dictionary
# values - will return all the values from the dictionary
# pop - will remove the key value from the dictionary - returns the value

# popitem - returns both key value from the dictionary
# setdefault - used to add new key values into the dictionary, will not allow us to modify the existing values

# update - updates values from a different dictionary, keys match values are overwritten, keys don't match it will be added as a new key value pair
