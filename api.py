import json
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})

@app.route('/lala', methods=['GET'])
def ping():
    return jsonify({'response': 'lele'})

app.run(host='0.0.0.0', port=5000)