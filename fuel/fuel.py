
while True:

    fuel = input("Fraction: ")
    try:
        numerator, demoninator = fuel.split('/')
        numerator = int(numerator)
        demoninator = int(demoninator)

        f = numerator / demoninator

        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
p = int(round(f*100))
if p <= 1:
    print("E")
elif p >=99:
    print("F")
else:
    print(f"{p}%")

