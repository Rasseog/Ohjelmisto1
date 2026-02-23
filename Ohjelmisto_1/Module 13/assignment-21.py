import mysql.connector

country_code = input("Enter country code (e.g. FI): ").upper()

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwerty7",
    database="flight_game"
)

cursor = connection.cursor()

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY type
"""

cursor.execute(sql, (country_code,))
results = cursor.fetchall()

if results:
    for airport_type, count in results:
        print(f"{airport_type}: {count}")
else:
    print("No airports found")

cursor.close()
connection.close()
