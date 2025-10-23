
def greet():
    print("Greetings Mr.Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")

# city is called as default argument and gname is non default arg
def greetGstCty(gname, city="Mumbai"):
    print(f"Greeting Mr.{gname} from {city}, Welcome to the event....")

greet()

print("-" * 60)

greetGst("Rahul")
greetGst("Virat")

print("-" * 60)

greetGstCty("Rohit")
greetGstCty("Hardik")
greetGstCty("Rahul", "Bangalore")

# functions with simple arguments

print("-" * 60)
def MyProduct(x, y):
    return x * y

print("%i * %i = %i" % (10, 20, MyProduct(10, 20)))

print("-" * 60)
# variable number of args

def productAll(*numbers):
    print(numbers)
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print("Multiply All = ", productAll(1, 2, 3, 4, 5))

print("-" * 60)

def extract_detials(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extract_detials(name='Sachin', age=34, runs=50, oppn="Newzeland")

print("-" * 60)
def basicArithematic(x, y):
    sum = x + y
    prod = x * y
    diff = x - y
    quot = x / y
    return sum, prod, diff, quot

res = basicArithematic(20, 8)
print(f"results :{res}")

print("-" * 60)
# named Tuple
# doc strings

"print('Hello World')"

def fun():
    # This is a comment
    "This is a doc string"
    print("hello world")

fun()
print(fun.__doc__)       # __doc__ - double underscore - dunder_doc

print("-" * 60)

def fun1(x, y):
    """
    function fun1(x, y)
    -------------------
    1. if x and y are integers then the function will return the sum of x and y
    2. if x and y are strings then the function will return the concatenated string of x and y
    3. if x and y are of different data types then it throws an error
    """
    return x + y

print(fun1(34, 75))
print(fun1("hello", "world"))
# print(fun1(10, "hello"))

print("-" * 60)
help(fun1)
