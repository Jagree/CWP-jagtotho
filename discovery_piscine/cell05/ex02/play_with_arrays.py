import random
arr = []
new_arr = []
for i in range(9):
    arr.append(random.randint(-1, 15))
print(f"{arr}")

for num in arr:
    if num > 5:
        new_arr.append(num + 2)
print(f"{new_arr}")