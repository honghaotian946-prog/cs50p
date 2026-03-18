import sys

if len(sys.argv) < 2:
    sys,exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[-1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1],"r",encoding="utf-8") as file:
        l = 0
        for line in file:
            if line.strip() and not line.strip().startswith("#"):
                l += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(l)


