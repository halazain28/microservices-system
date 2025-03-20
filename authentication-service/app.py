from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user database
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    credentials = request.json
    username = credentials.get('username')
    password = credentials.get('password')
    
    if username in users and users[username] == password:
        return jsonify({"status": "authenticated"}), 200
    else:
        return jsonify({"status": "unauthorized"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)