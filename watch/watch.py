import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"<iframe.*<\/iframe>", s):
        pattern = re.search(r"http[s]?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)", s)
        if pattern:
            split = pattern.groups()
            return "https://youtu.be/" + split[1]

if __name__ == "__main__":
    main()
