
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_detials = csv.reader(CSVR)

    # creating a pretty table object
    prtyTbl = PrettyTable(next(emp_detials))

    for row in emp_detials:
        prtyTbl.add_row(row)

print(prtyTbl)


"""
    col_name = next(emp_detials)
    print(*col_name)

    for row in emp_detials:
        print(*row)

"""