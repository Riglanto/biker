import pytest
import json

from app import app

@pytest.fixture
def client():
    client = app.app.test_client()
    yield client

def test_get_bikes(client):
	res = client.get('/bikes/stdev')
	data = json.loads(res.get_data(as_text=True))
	assert 'stdev' in data
