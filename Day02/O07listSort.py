
l1 = [7, 10, 4, 1, 9, 3, 5, 2, 8, 6]
print(f"l1 :{l1}")

asc_res = sorted(l1)
print(f"Ascending order :{asc_res}")

desc_res = sorted(l1, reverse=True)
print(f"Descending order :{desc_res}")

print("-" * 60)

l2 = [7, 'zebra', 'apple', 10, 'yellow', 'blue', 4, 'x_ray', 'dog', 1, 'white', 'maroon', 9, 'violet', 'green', 3, 'pink', 'horse', 5, 'island', 'orange', 2, 8, 6, 180, 1024, 29, 270, 2134]

print(f"l2 :{l2}")

print("-" * 60)
# res = sorted(l2, key=ascii)
# print(f"res :{res}")

res = sorted(l2, key=lambda x: (isinstance(x, str), x))
print(res)
