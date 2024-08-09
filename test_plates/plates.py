def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6 or plate[0].isalpha()== False  or plate[1].isalpha()== False:
        return False


    i = 0
    while i< len(plate):
        if plate[i].isalpha() == False:
            if plate[i] == "0":
                return False
            else:
                break
        i+=1
    characters =[".",",","!","?"]
    for char in plate:
        if char in characters:
            return False

    index = len(plate) - 1
    while index >= 0 and plate[index].isdigit():
        index -= 1

    first_part = plate[:index + 1]

    if any(char.isdigit() for char in first_part):
        return False


    return True

main()
