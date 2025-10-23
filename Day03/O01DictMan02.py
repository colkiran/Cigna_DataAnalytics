
player = {'name': 'Sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus'}
print(f"player :{player}")

# CRUD
print("-" * 60)
# read
print(f"player :{player}")

print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
# iteration

for x in player:
    print(f"{x}  => {player[x]}")

print("-" * 60)
# update - modify the existing data, add new key values
print(f"player :{player}")

player['name'] = 'Tendulkar'
player['age'] = 32

player['venue'] = 'Perth'
player['year'] = 2001
print(f"player :{player}")

print("-" * 60)
# delete
del player['age']
del player['year']

print(f"player :{player}")

#keys and values
print('keys'.center(60, "-"))
player = {'name': 'Tendulkar', 'age': 32, 'runs': 125, 'oppn': 'Aus', 'venue': 'Perth', 'year': 2001}
print(f"player :{player}")

ky = player.keys()
print(f"keys :{ky}")

for ky in player.keys():
    print(ky +  " => " + str(player[ky]))

print("values".center(60, "-"))

player = {'name': 'Tendulkar', 'age': 32, 'runs': 125, 'oppn': 'Aus', 'venue': 'Perth', 'year': 2001}
print(f"player :{player}")

vl = player.values()
print(f"values :{vl}")

print('items'.center(60, "-"))
player = {'name': 'Tendulkar', 'age': 32, 'runs': 125, 'oppn': 'Aus', 'venue': 'Perth', 'year': 2001}
print(f"player :{player}")

for k, v in player.items():
    print(k, "=>", v)

print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'hyd', 'pun', 'mum', 'del', 'kol']
print(f"Cities :{cities}")

res = dict.fromkeys(cities)
print(f'res :{res}')

res01 = dict.fromkeys(cities, 24)
print(f"res01 :{res01}")

# emp = {'empid': 'EMP001', 'empname': 'Mark', 'age': 35, 'desig': 'MGR', 'dept': 'finance', 'salary': 185000}
#
# print(f"emp :{emp}")
