def main():
    m = input()
    result = calculate(int(m))
    print(result)

def calculate(m):
    c= 300000000
    e = m * c * c
    return e

main()
