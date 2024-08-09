def main():

    eat_time = input("Enter the time: ")
    converted_time = convert(eat_time)

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    
    hour, minute = time.split(":")
    minute = float(minute) / 60
    float_time = float(hour) + minute
    return float_time

if __name__ == "__main__":
    main()
