#!/usr/bin/env python3
from flask import Flask, request
import redis
import requests
import json
from jobs import add_job, get_job_by_id, rd
# !NOTE! not importing the q or jdb client 

app = Flask(__name__)

# rd = redis.Redis(host='redis-db', port=6379, db=0)
url = 'https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json'
# change url

@app.route('/jobs', methods=['POST'])
def sumbmit_job():
    # do something with add_job
    data = request.get_json()
    job_dict = add_job(data['start'], data['end'])
    return job_dict
    
@app.route('/jobs/<jobid>', methods=['GET'])
def get_job(jobid):
    return get_job_by_id(jobid)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
