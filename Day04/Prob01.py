import csv

with open("EMP.csv", 'r') as CSVR:
    fileReader = csv.reader(CSVR)

    gender = {}
    desig = []
    dept = []
    salary = 0
    sal = 0

    for row in fileReader:
        # print(row)
        gen = row[2]

        if gen not in gender:
            gender[gen] = 1
        else:
            gender[gen] += 1

        des = row[3]

        if des not in desig:
            desig.append(des)

        dep = row[4]

        if dep not in dept:
            dept.append(dep)

        salary += int(row[5])

        if row[2] == 'f' and row[3] == 'MGR':
            sal += int(row[5])


print(gender)
print(desig)
print(dept)
print(salary)
print(sal)