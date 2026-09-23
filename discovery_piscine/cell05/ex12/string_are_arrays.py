import sys

if len(sys.argv) - 1 == 1 and sys.argv[1].count("z") >= 1:
    z = sys.argv[1].count("z")
    for i in range(z):
        print("z", end='')
    print()
else:
    print("none")