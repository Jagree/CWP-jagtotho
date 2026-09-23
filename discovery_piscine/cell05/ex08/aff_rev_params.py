import sys

sys.argv.reverse()
if len(sys.argv) > 2:
    for i in range(len(sys.argv) - 1):
        print(f"{sys.argv[i]}")
else:
    print("none")