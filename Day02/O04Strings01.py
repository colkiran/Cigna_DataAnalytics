st = "hello world"
print(f'st :{st}')
print(type(st))

print("-" * 60)
print(f"st :{st}")

print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st :{st}")

print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing using reverse indexing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# write to check if the given string is a palindrome using slicing
st = "malayalam"
print("Palindrome" if st[:] == st[::-1] else "Not Palindrome")

print("-" * 60)
# print(dir(st))
print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")

# length of a and b should be same
a = "helowrd"
b = "HELOWRD"

res_tbl = st.maketrans(a, b)
print(f"res_tbl :{res_tbl}")

print('translate'.center(60, '-'))
res = st.translate(res_tbl)

print(f"res :{res}")
