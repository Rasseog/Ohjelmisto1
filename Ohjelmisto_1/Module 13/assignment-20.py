import mysql.connector

icao = input("Enter ICAO code: ").upper()

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwerty7",        
    database="flight_game"
)

cursor = connection.cursor()

sql = """
SELECT name, municipality
FROM airport
WHERE ident = %s
"""

cursor.execute(sql, (icao,))
result = cursor.fetchone()

if result:
    print("Airport name:", result[0])
    print("Municipality:", result[1])
else:
    print("Airport not found")

cursor.close()
connection.close()
