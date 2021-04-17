import json

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db0"
mongo = PyMongo(app)

@app.route('/')
def root():
    return jsonify({'message': 'Valid route is /notes/<bug_id>'})

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

@app.route('/_bugs')
def get_bugs_with_notes():
    data = list(mongo.db.notes.find({}, limit=20))
    bugs = sorted(set([i.get('bug_id') for i in data]))
    return jsonify({'bugs': bugs})

@app.route('/notes/<bug_id>')
def get_notes(bug_id):
    data = list(mongo.db.notes.find({'bug_id': bug_id}, {'_id': 0}))
    if data:
        return jsonify({'bug_id': bug_id, 'notes': data[:10]})
    else:
        return {'error': f'No notes found for bug_id:{bug_id}'}, 404
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=23456)
