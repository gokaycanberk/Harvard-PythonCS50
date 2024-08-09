import inflect
p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        if name == "":
            break
        names.append(name)
    except EOFError:
        print("EOF received, exiting loop.")
        break

output = p.join(names)
print("Adieu, adieu, to " + output)
