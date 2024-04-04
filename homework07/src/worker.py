from jobs import get_job_by_id, update_job_status, q, rd
from hotqueue import HotQueue
import time

q = HotQueue("queue", host='redis-db', port=6379, db=1)

@q.worker
def do_work(jobid):
    update_job_status(jobid, 'in progress')
    time.sleep(30)   # rd.get() ... do some analysis
    update_job_status(jobid, 'complete')

do_work()
