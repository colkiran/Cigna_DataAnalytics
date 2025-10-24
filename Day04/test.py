
import csv

with open("test.csv", "r") as CSVR:
    reader = csv.DictReader(CSVR)
    for row in reader:
        print(row)
