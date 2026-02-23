names = set()

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.add(name)

for name in names:
    print(name)
