seasons = (
    "talvi",   # tammikuu
    "talvi",   # helmikuu
    "kevät",   # maaliskuu
    "kevät",   # huhtikuu
    "kevät",   # toukokuu
    "kesä",    # kesäkuu
    "kesä",    # heinäkuu
    "kesä",    # elokuu
    "syksy",   # syyskuu
    "syksy",   # lokakuu
    "syksy",   # marraskuu
    "talvi"    # joulukuu
)

month = int(input("Enter the month number (1-12): "))

if 1 <= month <= 12:
    print(seasons[month - 1])
else:
    print("Invalid month number")
