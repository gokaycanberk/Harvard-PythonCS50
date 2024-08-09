def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    answer = answer.lower()
    answer = answer.replace(" ","")

    if answer == 42 or answer == "42" or answer == "forty-two" or answer == "fortytwo":
        print("Yes")
    else:
        print("No")

main()
