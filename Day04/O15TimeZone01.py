
import time
from datetime import  datetime
import pytz

current_time = time.localtime()
print(f"current_time :{current_time}")
print("time is :", time.strftime("%H : %M :%S", current_time))

print("-" * 60)
tm1 = '9:32:56'
tm2 = "18:45:10"

print(f"tm1 :{tm1}")
print(type(tm1))

print("-" * 60)
print(f"tm2 :{tm2}")
print(type(tm2))

print("-" * 60)
tm1 = datetime.strptime(tm1, "%H:%M:%S")
print(f"login_time :{tm1}")
print(type(tm1))

print("-" * 60)
tm2 = datetime.strptime(tm2, "%H:%M:%S")
print(f"Logoff_time :{tm2}")
print(type(tm2))

timeDiff = tm2 - tm1
print(timeDiff)
