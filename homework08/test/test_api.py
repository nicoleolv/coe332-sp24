import pytest
from api import app

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

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_results(client):
    # test GET /results/<jobid> route
    response = client.get('/results/123')
    assert response.status_code == 200
    assert b'Job is still in progress' in response.data

def test_submit_job(client):
    # test POST /jobs route
    response = client.post('/jobs', json=sample_gene_data)
    assert response.status_code == 200
    assert b'status' in response.data

def test_get_job(client):
    # test GET /jobs/<jobid> route
    response = client.get('/jobs/123')
    assert response.status_code == 200
    assert b'job data' in response.data

def test_hgnc_data(client):
    # test GET /data route
    response = client.get('/data')
    assert response.status_code == 200
    assert b'data' in response.data

def test_hgnc_ids(client):
    # test GET /genes route
    response = client.get('/genes')
    assert response.status_code == 200
    assert b'genes' in response.data

def test_specific_hgnc_id(client):
    # test GET /genes/<hgnc_id> route
    response = client.get('/genes/123')
    assert response.status_code == 200
    assert b'gene data' in response.data

