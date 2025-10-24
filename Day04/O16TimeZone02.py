"""
UTC - Universal Time Coordinates
"""

from datetime import datetime
import time
import pytz

curtime = time.localtime()
curclock = time.strftime("%H:%M:%S", curtime)
print(curclock)

print("-" * 60)
utc = pytz.UTC
print(f"utc :{utc}")

print("-" * 60)
IST = pytz.timezone('Asia/Kolkata')
print(f"ist :{IST}")

print("-" * 60)
print("utc default format :", datetime.now(utc))

print("-" * 60)
print("ist default format :", datetime.now(IST))

print("-" * 60)
IST = pytz.timezone('Asia/Kolkata')
NYT = pytz.timezone('America/New_York')
UKT = pytz.timezone('Europe/London')
AST = pytz.timezone('Australia/Melbourne')

print("Indian Time              :", datetime.now(IST))
print("American Time            :", datetime.now(NYT))
print("United Kingdom Time      :", datetime.now(UKT))
print("Australian Time          :", datetime.now(AST))
