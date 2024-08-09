import csv
import sys


def main():
    check_command_line_argument()

    students = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if ',' not in row["name"]:
                    sys.exit(f"Invalid name: {row['name']}")
                slit_name = row["name"].split(',')
                students.append({"first": slit_name[1].strip(), "last": slit_name[0], "house": row["house"]})


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as a_file:
        writer = csv.DictWriter(a_file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in students:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def check_command_line_argument():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__== "__main__":
    main()
