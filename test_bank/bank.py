def main():
    greeting = input("Greeting: ")
    result = value(greeting)
    print(result)

def value(greeting):
    greeting = greeting.lower().strip()

    if 'hello' in greeting:
        return 0
    elif greeting[0] == 'h' and 'hello' not in greeting:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
