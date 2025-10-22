
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
print(dir(l1))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# copy, sort

# append - add one element at a time
# extend - add collection of values (list)
# insert - insert elements using the index
# clear - delete all the elements in the list - returns empty list
# count - count the no of times a values gets repeated in a list
# index - returns the index of a value (counts from the left)
# pop - remove elements from the list one at a time depending on the index provided, if index is not provided the last element of the list is removed, pop is the only function that will return the value that was removed from the list

# remove - remove the element from a list depending on the value specified
# reverse - reverses the list

l1 = ['a', 'b', 'c']
print(l1.index('c'))

print("copy".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 before :{l1}")

# copy the list l1 to l2
l2 = l1     # shallow copy - copies the address with data

print(f"l2 before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("-" * 60)
print("-" * 60)
print("-" * 60)

l3 = [5, 6, 7, 8, 9]
print(f"l3 before :{l3}")

# copy l3 to l4
l4 = l3.copy()          # deep copy - only data is shared
print(f"l4 before :{l4}")

l4.extend([10, 11, 12, 13])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("-" * 60)
print("-" * 60)
print("-" * 60)

l5 = [1, 2, 3, 4, [10, 20, 30], 5]
print(f"l5 before :{l5}")

# copy l5 to l6
l6 = l5.copy()
print(f"l6 before :{l6}")

l6[4].extend([40, 50, 60])
print(f"l6 after :{l6}")

print(f"l5 after :{l5}")

print("-" * 60)
print("-" * 60)
print("-" * 60)

l7 = [10, 20, [2, 4, 6, 8], 30, 40, 50]
print(f"l7 before :{l7}")

# copy l7 to l8
from copy import deepcopy
l8 = deepcopy(l7)

print(f"l8 before :{l8}")

l8[2].extend([10, 12, 14, 16])
print(f"l8 after :{l8}")

print(f"l7 after :{l7}")