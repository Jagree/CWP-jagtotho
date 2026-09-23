first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))
ans = first * second
print(f"{first} x {second} = {ans}")

if ans == 0:
    print("This number is both positive and negative.")
elif ans > 0:
    print("This number is positive.")
else:
    print("This number is negative.")
print()