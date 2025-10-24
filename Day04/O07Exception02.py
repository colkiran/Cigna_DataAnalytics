

try:
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number:"))

    res = num1 / num2

except (ZeroDivisionError, TypeError, ValueError) as x:
    print('Error caught......')
    print(x)

# except ZeroDivisionError as e:
#     print("ZeroDivisionError occured.....")
#     print(e)
#
# except TypeError as t:
#     print("TypeError occured....")
#     print(t)

else:
    print(f"results :{res}")

finally:
    print(f"finally code.....")