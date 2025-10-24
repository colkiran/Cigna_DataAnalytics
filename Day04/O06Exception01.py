
import sys

num = int(input("Enter the first number :"))
divisor = 0
try:
    res = num / divisor
    print(f"results :{res}")
except:
    print("except caught.....")

    # error class
    print(sys.exc_info()[0])

    # error message
    print(sys.exc_info()[1])
