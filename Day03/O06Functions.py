from collections import namedtuple

def basicArithematic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    result = namedtuple("Results", "sum diff prod quot")
    curren_result = result(sum = sum, diff = diff, prod=prod, quot = quot)
    return  curren_result

print(basicArithematic(200, 80))