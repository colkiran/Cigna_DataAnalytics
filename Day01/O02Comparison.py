
print("Arithmetic Operator")
print(f"Sum: 10 + 3 = {10 + 3}")
print(f"(Sub: 10 - 3 = {10 - 3}")
print(f"Prod: 10 * 3 = {10 * 3}")
print(f"Quot : 10 / 3 = {10 / 3}")
print(f"floor : 10 // 3 :{10 // 3}")
print(f"Modulus :10 % 3 :{10 % 3}")
print(f'Power :10 ** 3 :{10 ** 3}')

print("Augmentor".center(60, "-"))
x = 10
print(f"x :{x}")
x += 5
print(f"x :{x}")
x /= 3
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# ==, !=, <, <=, >, >=
a = 10
b = 20
print(f"a == b :{a == b}")
print(f"a > b  :{a > b}")
print(f"a < b  :{a < b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(60, "-"))
# and, or, not

print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")

print(f"1 == 1 or 2 == 2 :{not(1 == 1 or 2 == 2)}")
print(f"1 == 2 or 2 == 1 :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")  # integer representation of unicode character
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("-" * 60)
print(f"chr(97) :{chr(97)}")
print(f"chr(122) :{chr(122)}")
print(f"chr(65) :{chr(65)}")
print(f"chr(90) :{chr(90)}")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
