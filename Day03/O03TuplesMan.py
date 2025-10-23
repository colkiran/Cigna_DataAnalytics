
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3, 'four', 'five', 'six', 7.2, 8.9, 9.0, 10+2j, 11-2j)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(10, 101, 10))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 10,
print(f't4 :{t4}')
print(type(t4))

print("-" * 60)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 60)
# print(dir(t1))
t1 = (1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2 ,2, 2, 2, 2, 2, 2, 2, 2, 2, 2 , 2)
print(f"t1 :{t1}")

# count
print(f"1 :{t1.count(1)}")
print(f"2 :{t1.count(2)}")
print(f"3 :{t1.count(3)}")
print(f"8 :{t1.count(8)}")

print("-" * 60)
# index
print("First 3 :", t1.index(3))
print("Second 3 :", t1.index(3, t1.index(3) + 1))
print("Third 3 :", t1.index(3, t1.index(3, t1.index(3) + 1 ) + 1))