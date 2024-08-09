def main():
    user_input = input("Input: ")
    result = remove_vowels(user_input)
    print(result)


def shorten(user_input):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for char in user_input:
        if char not in vowels:
            result += char
    return result

main()
