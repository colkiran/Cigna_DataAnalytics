
num1 = int(input("Enter the first number :"))
print(f"num1 :{num1}")
print(type(num1))

if num1 < 10: print(f"num1 is a single digit number :{num1}")

num2 = int(input("Enter the second number :"))
print(f"num2 :{num2}")

num3 = int(input("Enter the second number :"))
print(f"num2 :{num3}")

if num1 >= num2 and num1 >= num3:
    print(f"num1 is the greatest :{num1}")
elif (num2 >= num1 and num2 >= num3):
    print(f"num2 is the greatest :{num2}")
else:
    print(f"num3 is the greatest :{num3}")
