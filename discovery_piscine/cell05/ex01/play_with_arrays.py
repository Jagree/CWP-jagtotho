import random
arr = []
new_arr = []
for i in range(9):
    arr.append(random.randint(-5, 10))
print(f"Original array: {arr}")

for i in range(len(arr)):
    new_arr.append(arr[i] + 2)
print(f"New array: {new_arr}")