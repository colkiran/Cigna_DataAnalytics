
for i in range(1, 11):
    print(i, end=" ")

print()         # prints a new line

print("-" * 60)

for i in range(1, 30):
    # if i > 25:
    #     break
    if i % 2 == 1:
        continue        # skip the current iteration
    else:
        print(i, end=" ")
else:
    print("\ncompleted generating numbers")