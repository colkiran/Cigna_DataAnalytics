import mypackage.mymodule as m

from mypackage.mymodule import Employee

m.greet("Rahul")

emp1 = Employee("Richard", 85000)
print(emp1)        # calls __str__