from flask import Flask, request, jsonify
import mysql.connector
import time
from mysql.connector import Error
from flask_cors import CORS #

app = Flask(__name__)
CORS(app)  #

# MySQL configuration
db_config = {
    'host': 'mysql-db',
    'user': 'root',
    'password': 'root',
    'database': 'data_db'
}

def connect_to_mysql():
    retries = 10  
    delay = 10 
    for i in range(retries):
        try:
            connection = mysql.connector.connect(**db_config)
            return connection
        except Error as e:
            print(f"Attempt {i + 1} failed: {e}")
            time.sleep(delay)
    raise Exception("Could not connect to MySQL after multiple attempts")

@app.route('/enter', methods=['POST'])
def enter_data():
    data = request.json
    try:
        connection = connect_to_mysql()
        cursor = connection.cursor()
        query = "INSERT INTO data_table (value) VALUES (%s)"
        cursor.execute(query, (data['value'],))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"status": "success"}), 200
    except Error as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)