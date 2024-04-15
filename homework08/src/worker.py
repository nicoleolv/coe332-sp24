from jobs import get_job_by_id, update_job_status, q, rd, res
from hotqueue import HotQueue
import time
import json

q = HotQueue("queue", host='redis-db', port=6379, db=1)

@q.worker
def do_work(jobid):
    """
    Calls the analyze function to do work based on start and end date
    """
    try:
        update_job_status(jobid, 'in progress')
        # retrieves the data
        job_data = get_job_by_id(jobid)
    
        start_date = job_data['start_date']
        end_date = job_data['end_date']

        analysis_results = analyze(start_date, end_date)

        res.set(jobid, json.dumps(analysis_results))
        
        update_job_status(jobid, 'complete')

    except raise ValueError:
        update_job_status(jobid, 'failed')
        print(f"Invalid jobid provided.")
        
def analyze(start_date, end_date):
    """
    Performs analysis to count the number os approved genes within a specified date range
    """
    genes_in_date_range = [json.loads(rd.get(key)) for key in rd.keys() if start_date <= json.loads(rd.get(key))['date_modified'] <= end_date]
    
    for gene in genes_in_date_range:
        if gene.get('status') == 'Approved':
            approved_genes += 1
    return {"Amount of genes approved within the date range:": approved_genes} 
    
do_work()
