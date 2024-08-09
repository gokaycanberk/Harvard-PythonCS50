def main():
    user_input = input("Input: ")
    result = shorten(user_input)
    print("Output: " + result)

def shorten(user_input):
    word_without_vowels = ""
    for letter in user_input:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            word_without_vowels += letter
    return word_without_vowels

if __name__ == "__main__":
    main()
