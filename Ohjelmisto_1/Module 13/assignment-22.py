import mysql.connector
from geopy.distance import geodesic


def get_coordinates(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Qwerty7",
        database="flight_game"
    )

    cursor = connection.cursor()

    sql = """
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE ident = %s
    """
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


icao1 = input("Enter the ICAO code of the first airport: ").upper()
icao2 = input("Enter the ICAO code of the second airport: ").upper()

coords1 = get_coordinates(icao1)
coords2 = get_coordinates(icao2)

if coords1 and coords2:
    distance_km = geodesic(coords1, coords2).kilometers
    print(f"Distance between {icao1} and {icao2}: {distance_km:.2f} km")
else:
    print("One or both airports were not found.")
