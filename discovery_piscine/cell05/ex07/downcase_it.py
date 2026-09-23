import sys

print(f"{sys.argv[1].lower() if len(sys.argv) - 1 == 1 else "none"}")