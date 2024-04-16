import pytest
from jobs import add_job, get_job_by_id, update_job_status

sample_gene_data = [
    {
        "hgnc_id": "HGNC:123",
        "symbol": "GENE1",
        "name": "Gene 1",
        "status": "Approved",
        "date_modified": "2023-01-01",
        "other_key": "other_value"
    },
    {
        "hgnc_id": "HGNC:456",
        "symbol": "GENE2",
        "name": "Gene 2",
        "status": "Approved",
        "date_modified": "2023-02-01",
        "other_key": "other_value"
    },
    {
        "hgnc_id": "HGNC:789",
        "symbol": "GENE3",
        "name": "Gene 3",
        "status": "Withdrawn",
        "date_modified": "2023-03-01",
        "other_key": "other_value"
    }
]

def test_add_job():
    # test add_job function
    job_dict = add_job(sample_gene_data[0]['date_modified'], sample_gene_data[1]['date_modified'])
    assert 'id' in job_dict
    assert job_dict['status'] == 'submitted'

def test_get_job_by_id():
    # test get_job_by_id function
    job_data = get_job_by_id('123')
    assert job_data['id'] == '123'
    assert 'status' in job_data

def test_update_job_status():
    # test update_job_status function
    with pytest.raises(Exception):
        update_job_status('invalid_job_id', 'completed')
