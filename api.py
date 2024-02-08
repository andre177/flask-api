import json
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    response = jsonify({'response': 'pong'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/health', methods=['GET'])
def healthcheck():
    response = jsonify({'status': 'ok'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

app.run(host='0.0.0.0', port=5000)