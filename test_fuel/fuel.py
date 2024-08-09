def main():
    fraction = input("Fraction: ")
    fraction_convert = convert(fraction)
    output = gauge(fraction_convert)
    print(output)

def convert(fraction):
    while True:
        try:
            numerator, demoninator = fraction.split('/')
            numerator = int(numerator)
            demoninator = int(demoninator)

            fraction = numerator / demoninator

            if fraction <= 1:
                p= int(fraction*100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if ppercentage <= 1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()







