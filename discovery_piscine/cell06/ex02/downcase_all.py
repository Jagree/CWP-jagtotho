import sys

def downcase_it(text):
    return text.lower()

if len(sys.argv) - 1 > 0:
    for i in range(1, len(sys.argv)):
        print(downcase_it(sys.argv[i]))
else:
    print("none")