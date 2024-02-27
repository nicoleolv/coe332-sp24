import pytest
from datetime import datetime
from iss_tracker import parseXML, get_epochs, epochs, specific_epoch, instantaneous_speed, nearest_epoch
from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)
    yield app

@pytest.fixture
def mock_data():
    return [{'epoch': datetime(2024, 2, 16, 12, 0), 'x_dot': 1.0, 'y_dot': 2.0, 'z_dot': 3.0}]

def test_parseXML(mock_data, tmp_path):
    sample_xml_content = """
    <root>
        <stateVector>
            <EPOCH>2024-047T12:00:00.000Z</EPOCH>
            <X_DOT>1.0</X_DOT>
            <Y_DOT>2.0</Y_DOT>
            <Z_DOT>3.0</Z_DOT>
        </stateVector>
    </root>
    """
    xml_file = tmp_path / "test.xml"
    with open(xml_file, "w") as f:
        f.write(sample_xml_content)

    data = parseXML(xml_file)

    assert len(data) == 1
    assert data[0]['epoch'] == datetime(2024, 2, 16, 12, 0)
    assert data[0]['x_dot'] == 1.0
    assert data[0]['y_dot'] == 2.0
    assert data[0]['z_dot'] == 3.0

def test_instantaneous_speed(mock_data):
    with Flask(__name__).test_request_context():
        speed = instantaneous_speed('2024-047T12:00:00.000Z')
        assert speed == "3.7416573867739413"

def test_get_epochs(mock_data, app):
    with app.test_request_context():
        expected_data = mock_data
        response = get_epochs()
        assert response.json == expected_data

def test_epochs(mock_data, app):
    with app.test_request_context():
        expected_data = mock_data
        response = epochs(1, 0)
        assert response.json == expected_data

def test_specific_epoch(mock_data):
    expected_data = mock_data[0]
    response = specific_epoch('2024-047T12:00:00.000Z')
    assert response == expected_data

def test_nearest_epoch(mock_data, app):
    with app.test_request_context():
        expected_data = mock_data[0]
        response = nearest_epoch()
        assert response.json == expected_data
