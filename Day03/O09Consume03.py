
import sys

for pth in sys.path:
    print(pth)

print("-" * 60)

from gurgaon.mymodule import Employee

emp = Employee('Kevin', 85000)
print(emp)