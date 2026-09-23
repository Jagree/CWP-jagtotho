import sys

if len(sys.argv) - 1 == 1:
    text = sys.argv[1]
else:
    print("none")

user_inp = input("What was the parameter? ")
if user_inp == text:
    print("Good job!")
else:
    print("Nope, sorry...")