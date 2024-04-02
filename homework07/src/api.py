#!/usr/bin/env python3
from flask import Flask, request, jsonify
import redis
import requests
import json
from jobs import add_job, get_job_by_id, rd
# !NOTE! not importing the q or jdb client 

app = Flask(__name__)

# rd = redis.Redis(host='redis-db', port=6379, db=0)
url = 'https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json'
# change url

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def hgnc_data():
    if request.method == 'GET':
        # read all data out to Redis and return it as a JSON list
        data = [json.loads(rd.get(key)) for key in rd.keys()]
        return jsonify(data), 200
    
    elif request.method == 'POST':
        # load the HGNC data to a redis database
        reponse = requests.get(url)
        data = reponse.json()['response']['docs']
        for item in data:
            rd.set(item['hgnc_id'], json.dumps(item))
        return 'Data loaded into Redis successfully\n', 200

    elif request.method == 'DELETE':
        # delete all data from redis
        rd.flushdb()
        return 'Data deleted from Redis succesfully\n', 200

@app.route('/genes', methods=['GET'])
def hgnc_ids():
    """
    Returns json-formatted list of all hgnc_ids
    """
    keys = rd.keys()
    gene_data = []
    for key in keys:
        gene_id = key.decode('utf-8')
        gene = rd.get(key)
        gene_data.append({gene_id: json.loads(gene)})
    return jsonify(gene_data), 200
        
@app.route('/genes/<hgnc_id>', methods=['GET'])
def specific_hgnc_id(hgnc_id):
    """
    Returns all data associated with the given hgnc_id
    """
    gene_data = rd.get(hgnc_id)
    if gene_data:
        return gene_data, 200
    else:
        return 'Gene ID not found\n', 404

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
    app.run(debug=True, host='0.0.0.0', port=5001)
