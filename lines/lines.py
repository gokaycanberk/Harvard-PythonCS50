import sys


def main():
    check_command_line_argument()

    with open(sys.argv[1], "r") as file:
        count_lines = 0
        for line in file:
            if not check_comment_line(line):
                count_lines += 1
        print(count_lines)

def check_comment_line(line):
    if line.isspace() or line.lstrip().startswith("#"):
        return True
    else:
        return False

def check_command_line_argument():
    if len(sys.argv) <2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


if __name__== "__main__":
    main()



