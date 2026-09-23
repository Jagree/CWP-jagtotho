import sys

arr = []
if len(sys.argv) - 1 == 0:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) < 3 or sys.argv[i][-3] + sys.argv[i][-2] + sys.argv[i][-1] != "ism":
            arr.append(sys.argv[i] + "ism")

    if arr != []:
        for item in arr:
            print(item)
    else:
        print("none")