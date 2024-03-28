# backend/app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://user01:tCaHp899bRnMbyMJ@mlopstask05.phedrla.mongodb.net/')
db = client['mlopstask05']
collection = db['users']

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    collection.insert_one(data)
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
