import sys

arr = []
if len(sys.argv) - 1 != 2:
    print("none")
else:
    try:
        start, end = int(sys.argv[1]), int(sys.argv[2])
        for i in range(start, end + 1):
            arr.append(i)
        print(arr)
    except:
        print("none")