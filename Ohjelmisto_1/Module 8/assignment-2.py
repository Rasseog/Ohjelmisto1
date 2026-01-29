import csv

from collections import defaultdict


def get_airports_by_country(country_code):

    airport_counts = defaultdict(int)

    csv_path = r'C:\Users\joona\Downloads\airports.csv'

    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                if row['iso_country'] == country_code:
                    airport_counts[row['type']] += 1

        if airport_counts:
            # Sort by count (descending)
            sorted_airports = dict(sorted(airport_counts.items(),
                                          key=lambda x: x[1],
                                          reverse=True))
            return sorted_airports
        return None

    except FileNotFoundError:
        print(f"Error: Could not find airports.csv at {csv_path}")
        return None

def run_country_program():

    country_code = input("Enter the country code (e.g., FI for Finland): ").upper()

    airports = get_airports_by_country(country_code)

    if airports:
        print(f"\nAirports in {country_code}:")
        for airport_type, count in airports.items():
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for country code {country_code}.")

if __name__ == "__main__":
    run_country_program()