import emoji


def main():


    user_input = input("Input: ")
    user_input = user_input.split()

    for word in user_input:

        print(emoji.emojize(word, language='alias'), end=" ")

    print()


main()
