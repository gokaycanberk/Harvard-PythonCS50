import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if " to " not in s:
        raise ValueError
    isCorrect = re.search(r"^([01]?[0-9]|2[0-3]):*([0-5][0-9])* ([A-P]M) to ([01]?[0-9]|2[0-3]):*([0-5][0-9])* ([A-P]M)$", s)
    if isCorrect:
        split = isCorrect.groups()
        if int(split[0])> 12 or int(split[3])> 12:
            raise ValueError
        first_time = new_format(split[0],split[1],split[2])
        last_time = new_format(split[3],split[4],split[5])
        return first_time + ' to ' + last_time
    else:
        raise ValueError

def new_format(hour,minute,am_PM):
    if am_PM == 'PM':
        if int(hour) == 12:
            new_hour =12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ':00'
    else:
        new_minute = ':' + minute
    new_time = str(new_hour).zfill(2) + new_minute

    return new_time

if __name__ == "__main__":
    main()
