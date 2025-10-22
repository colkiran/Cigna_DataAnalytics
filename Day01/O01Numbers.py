
a = 10
b = -1
print(f"a :{a}")        # interpolation - format string
print(type(a))          # RTTI - Runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.0
d = -10.5
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = 2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3 + 2j
h = 3 - 4j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

def Mx(*lst):
    return max(lst), type(lst)

print("-" * 60)
print(10, 30, 50, 35, 25, 65, 45)
print(f"Max :{Mx(10, 30, 50, 35, 25, 65, 45)}")
print(f"Min :{min(10, 30, 50, 35, 25, 65, 45)}")

print("-" * 60)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

print("-" * 60)
x = 2
y = 3.5
z = x + y

print("x = ", type(x))
print("y = ", type(y))
print("z = ", type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(f"11 :{11}")          # decimal number
print(f"0b11  :{0b11}")      # binary number
print(f"0b101 :{0b101}")     # binary
print(f"0o11  :{0o11}")      # octal
print(f"0o101 :{0o101}")     # octal
print(f"0xa  :{0xa}")        # hexa
print(f"0xe  :{0xe}")        # hexa

print("number system conversion".center(60, '-'))
a = 100
print(f"oct(a) :")
print(f"hex(a) :{hex(a)}")
print(f"oct(b) :{oct(b)}")