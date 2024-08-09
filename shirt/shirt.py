import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_argument()


    # Open the image
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # open shirt

    shirt = Image.open("shirt.png")

    size = shirt.size
    muppet = ImageOps.fit(image, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


def check_command_line_argument():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if check_file_extension(file1) == False:
        sys.exit("Invalid input")
    if check_file_extension(file2) == False:
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")



def check_file_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True




if __name__== "__main__":
    main()
