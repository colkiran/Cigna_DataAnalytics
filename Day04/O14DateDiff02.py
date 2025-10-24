
from datetime import datetime
import dateutils

dt1 = "Wednesday, September 30, 2020"
print(f"dt1 :{dt1}")
print(type(dt1))

print("-" * 60)
dt2 = "Sunday, October 31, 2021"
print(f"dt2 :{dt2}")
print(type(dt2))

print("-" * 60)
actdt1 = datetime.strptime(dt1, "%A, %B %d, %Y")
print(f"actdt1 :{actdt1}")
print(type(actdt1))

print("-" * 60)
actdt2 = datetime.strptime(dt2, "%A, %B %d, %Y")
print(f"actdt2 :{actdt2}")
print(type(actdt2))

print("-" * 60)
print(f"No of Days :{actdt2 - actdt1}")

print("-" * 60)
print(f"No of Days :{dateutils.days(actdt2, actdt1)}")

print("-" * 60)
print(f"Difference in weeks :{dateutils.weeks(actdt2, actdt1)}")

print("-" * 60)
print(f"Difference in months :{dateutils.months(actdt2, actdt1)}")

print("-" * 60)
print(f"Difference in years :{dateutils.years(actdt2, actdt1)}")
