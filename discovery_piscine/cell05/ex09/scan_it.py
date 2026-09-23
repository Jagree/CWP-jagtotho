import sys

if len(sys.argv) - 1 == 2:
    print(f"{sys.argv[2].count(sys.argv[1])}")
else:
    print("none")