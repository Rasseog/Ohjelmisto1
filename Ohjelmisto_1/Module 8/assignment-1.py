import csv

icao_code = input("Enter the ICAO code of an airport: ").upper()

found = False
with open('C:/Users/joona/Downloads/airports.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        if row['ident'] == icao_code:
            print(f"Airport name: {row['name']}")
            print(f"Location: {row['municipality']}")
            found = True
            break

if not found:
    print(f"No airport found with ICAO code {icao_code}")