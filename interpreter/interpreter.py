def main():
    expression = input("Enter an expression: ")
    x, y, z = expression.split(" ")

    result = calculate(x,y,z)
    print(result)
def calculate(x, y, z):
    x = float(x)
    z = float(z)

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "/":
        return x / z
    else:
        return x * z

main()
