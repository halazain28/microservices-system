from flask import Flask
import mysql.connector
from pymongo import MongoClient

app = Flask(__name__)

# MySQL configuration
mysql_config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql-db',
    'database': 'data_db'
}

# MongoDB configuration
mongo_client = MongoClient('mongo-db', 27017)
mongo_db = mongo_client.analytics_db
mongo_collection = mongo_db.results

def calculate_statistics():
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(value), MIN(value), AVG(value) FROM data_table")
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    
    stats = {
        'max': result[0],
        'min': result[1],
        'avg': result[2]
    }
    
    mongo_collection.insert_one(stats)

if __name__ == '__main__':
    calculate_statistics()
    app.run(host='0.0.0.0', port=5003)