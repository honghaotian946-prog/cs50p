import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys,exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[-1].endswith(".csv"):
    sys.exit("Not a CSV file")

orders = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
             orders.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(orders,headers = "keys",tablefmt = "grid"))



