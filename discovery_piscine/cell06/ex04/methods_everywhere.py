import sys

def shrink(text):
    return text[slice(8)]

def enlarge(text):
    while len(text) < 8:
        text += "z"
    return text

if len(sys.argv) - 1 > 0:
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) > 8:
            print(shrink(sys.argv[i]))
        elif len(sys.argv[i]) < 8:
            print(enlarge(sys.argv[i]))
        else:
            print(sys.argv[i])
else:
    print("none")