import argparse
import sys
from pyfiglet import Figlet
from random import choice

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--font', help='The font to use')

args = parser.parse_args()

figlet = Figlet()

if args.font:
    if args.font in figlet.getFonts():
        figlet.setFont(font=args.font)
    else:
        sys.exit(f"Invalid usage")
else:
    figlet.setFont(font=choice(figlet.getFonts()))

text = input("Input: ")

# Output the text in the desired font
print(figlet.renderText(text))
