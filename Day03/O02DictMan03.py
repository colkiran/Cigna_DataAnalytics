
print("setdefault".center(60, "-"))
emp = {'empname': 'Slater', 'age': 32, 'dept':'HR', 'sal': 125000 }
print(f"emp :{emp}")
emp.setdefault('dept', 'bin'),
emp.setdefault('age', 20),
emp.setdefault('empname', 'Jack'),
emp.setdefault('sal', 25000)
emp.setdefault('empid', 'EMP001')

print(f"emp :{emp}")

print("pop".center(60, "-"))
emp = {'empname': 'Slater', 'age': 32, 'dept':'HR', 'desig': 'BDM', 'sal': 125000 }
print(f"emp :{emp}")

res = emp.pop('dept')
print(f"res :{res}")

res = emp.pop('sal')
print(f"res :{res}")

# res = emp.pop()
# print(f"res :{res}")
print(F"emp :{emp}")

print("popitem".center(60, "-"))

emp = {'empname': 'Slater', 'age': 32, 'dept':'HR', 'desig': 'BDM', 'sal': 125000 }
print(f"emp :{emp}")

res = emp.popitem()
print(res)

print(f'emp :{emp}')

print("update".center(60, "-"))
emp1 = {'empname': 'Slater', 'age': 32, 'dept':'HR', 'sal': 125000 }

emp2 = {'empname': 'Jill', 'age': 28, 'dept':'Finance', 'desig': 'Fin_Exe', 'sal': 59000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 60)
# update the values of emp1 from emp2

emp1.update(emp2)
print(f"emp1 :{emp1}")
