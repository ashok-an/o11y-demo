import json
import os
import random
import time

import redis
import requests
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_api_cache import ApiCache

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv('MONGODB_URI') or "mongodb://localhost:27017/db0"
mongo = PyMongo(app)


redis_host = os.getenv('REDIS_HOST') or 'localhost'
redis_port = os.getenv('REDIS_PORT') or '6379'
redis_instance = redis.StrictRedis(host=redis_host, port=redis_port)


def get_notes(bug_id):
    url_base = os.getenv('NOTES_BASE_URL') or 'http://localhost:23456'
    r = requests.get(f'{url_base}/notes/{bug_id}')
    if r.ok:
        return r.json().get('notes', [])
    else:
        return []


@app.route('/')
def root():
    return jsonify({'message': 'Valid route is /bugs?user_id=<string>&bug_id=<string>'})

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

@app.route('/bugs')
@ApiCache(redis=redis_instance, expired_time=15)
def get_bugs():

    time.sleep(random.uniform(1, 3))

    params = {}
    user_id = request.args.get('user_id')
    if user_id:
        params['engineer'] = user_id

    bug_id = request.args.get('bug_id')
    if bug_id:
        params['_id'] = bug_id

    data = mongo.db.bugs.find(params, limit=10)
    output = []
    for i in data:
        i['notes'] = get_notes(i.get('_id'))
        output.append(i)

    if output:
        return jsonify({'params': params, 'bugs': output})
    else:
        return {'error': f'No bugs found for criteria:{params}'}, 404
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12345)
