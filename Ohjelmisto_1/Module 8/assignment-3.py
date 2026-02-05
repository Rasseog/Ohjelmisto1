import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",        # vaihda tarvittaessa
        password="",        # vaihda tarvittaessa
        database="flight_game"
    )

    cursor = connection.cursor()

    query = """
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE ident = %s
    """
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


def run_airport_distance():
    icao1 = input(
        "Enter the ICAO code of the first airport: "
    ).upper()
    icao2 = input(
        "Enter the ICAO code of the second airport: "
    ).upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if not coords1 or not coords2:
        print(f"Airport with ICAO code {icao1 or icao2} not found in the database.")
        return

    distance_km = geodesic(coords1, coords2).kilometers

    print(
        f"\n\nDistance between {icao1} and {icao2}: "
        f"{distance_km:.2f} kilometers"
    )


# Käynnistetään ohjelma
run_airport_distance()
