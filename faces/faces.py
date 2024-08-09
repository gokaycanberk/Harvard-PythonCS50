def main():
    message = input()
    result = convert(message)

    print(result)

def convert(message):
    message = message.replace(":)","🙂")
    message = message.replace(":(","🙁")
    return message


main()


