fibo = int(input("Enter the number of terms"))

# First two terms
a = 0
b = 1

print("Fibonacci series:")
print(a, end=' ')
if fibo > 1:
    print(b, end=' ')

# Generate the rest of the series
for _ in range(2, fibo):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
