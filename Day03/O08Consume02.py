import sys

sys.path.append("C:/Delhi")

for pth in sys.path:
    print(pth)
    
from gurgaon.mymodule import Employee
emp1 = Employee("Rahul", 45000)
print(emp1)
# print(sys.path)
