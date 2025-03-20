from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS  # 

app = Flask(__name__)
CORS(app)  # 

# MongoDB configuration
client = MongoClient('mongo-db', 27017)
db = client.analytics_db
collection = db.results

@app.route('/results', methods=['GET'])
def show_results():
    results = list(collection.find({}, {'_id': 0}))
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)