from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_airport(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",          # vaihda tarvittaessa
        password="",          # vaihda tarvittaessa
        database="flight_game"
    )

    cursor = connection.cursor()
    sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
    """
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

@app.route("/kenttä/<icao>", methods=["GET"])
def airport_info(icao):
    icao = icao.upper()
    result = get_airport(icao)

    if result:
        response = {
            "ICAO": icao,
            "Name": result[0],
            "Municipality": result[1]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)