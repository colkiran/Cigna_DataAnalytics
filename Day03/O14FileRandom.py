
FL = open("data.txt", "rb")

print(FL.tell())

pos = FL.seek(150, 0)
print(f"position :{pos}")

pos = FL.seek(165, 1)
print(f"position :{pos}")

pos = FL.seek(-280, 1)
print(pos)

print(FL.seek(0, 2))

FL.close()