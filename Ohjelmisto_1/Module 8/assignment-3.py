import csv
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):

    with open('C:/Users/joona/Downloads/airports.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row['ident'] == icao_code:
                # Return coordinates as tuple (latitude, longitude)
                latitude = float(row['latitude_deg'])
                longitude = float(row['longitude_deg'])
                return (latitude, longitude)

    return None

def run_airport_distance():

    icao1 = input("Enter the ICAO code of the first airport: ").upper()
    icao2 = input("Enter the ICAO code of the second airport: ").upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if coords1 is None:
        print(f"Airport {icao1} not found.")
        return

    if coords2 is None:
        print(f"Airport {icao2} not found.")
        return

    distance = geodesic(coords1, coords2).kilometers

    print(f"\nDistance between {icao1} and {icao2}: {distance:.2f} kilometers")

if __name__ == "__main__":
    run_airport_distance()