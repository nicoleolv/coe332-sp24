import pytest
from worker import analyze


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

def test_analyze():
    # test analyze function
    result = analyze(sample_gene_data)
    assert result == expected_result
