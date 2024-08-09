def main():
    message = input("Greeting: ")
    result = check_message(message)
    print(result)

def check_message(message):
    message = message.replace(" ", "")
    message = message.lower()
    first_five_letters = message[:5]

    if first_five_letters == "hello":
        return("$0")
    elif message[0] == "h":
        return("$20")
    else:
        return("$100")

main()
