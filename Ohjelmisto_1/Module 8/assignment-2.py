import mysql.connector


def get_airports_by_country(country_code):
    """
    Hakee lentokentät maakoodin perusteella ja ryhmittelee ne tyypin mukaan.

    Args:
        country_code (str): Maakoodi (esim. "FI")

    Returns:
        list: Lista tupleja (tyyppi, määrä)
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="flight_game"
    )
    cursor = connection.cursor()

    query = """
            SELECT type, COUNT(*)
            FROM airport
            WHERE iso_country = %s
            GROUP BY type
            ORDER BY type \
            """

    cursor.execute(query, (country_code,))
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


def run_country_program():
    """Pääohjelma - kysyy maakoodin ja tulostaa lentokentät"""

    country_code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()

    airports = get_airports_by_country(country_code)

    if not airports:
        print(f"No airports found for country code '{country_code}'.")
        return

    print(f"\n\nAirports in {country_code}:")
    for airport_type, count in airports:
        print(f"{count} {airport_type} airports")


# Suorita ohjelma
run_country_program()