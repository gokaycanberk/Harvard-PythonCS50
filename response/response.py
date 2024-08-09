import validators


def main():

    print(validate_email(input("Enter email: ")))


def validate_email(email: str) -> bool:
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"



if __name__ == "__main__":
    main()
