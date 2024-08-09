import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or int(octet) > 255 or int(octet) < 0:
            return False
    return True


if __name__ == "__main__":
    main()
