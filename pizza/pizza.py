import csv
import tabulate
import json
import sys


def main():
    check_command_line_argument()

    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        data = list(reader)
    print(tabulate.tabulate(data, headers="firstrow", tablefmt="grid"))

def check_command_line_argument():
    if len(sys.argv) <2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif sys.argv[1] != "regular.csv" and sys.argv[1] != "sicilian.csv":
        sys.exit("File does not exist")


if __name__== "__main__":
    main()
