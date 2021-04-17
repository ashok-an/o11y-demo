import json

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db0"
mongo = PyMongo(app)

@app.route('/')
def root():
    return jsonify({'message': 'Valid route is /bugs?user_id=<string>&bug_id=<string>'})

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

@app.route('/bugs')
def get_all_bugs():
    params = {}
    user_id = request.args.get('user_id')
    if user_id:
        params['engineer'] = user_id

    bug_id = request.args.get('bug_id')
    if bug_id:
        params['_id'] = bug_id

    data = list(mongo.db.bugs.find(params, limit=20))
    if data:
        return jsonify({'params': params, 'bugs': data[:10]})
    else:
        return {'error': f'No bugs found for criteria:{params}'}, 404
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12345)
