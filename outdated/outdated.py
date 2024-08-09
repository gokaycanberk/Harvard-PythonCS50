

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

while True:
    try:
        date = input("Date: ")
        date = date.strip()  # Remove leading and trailing spaces
        month, day, year = date.split("/")
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    except ValueError:
        try:
            if(date.find(",") == -1):
                raise ValueError
            month, day, year = date.replace(",", "").split(" ")
            day = day.replace(",", "")
            month = months.index(month) + 1
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
        except ValueError:
            print()

