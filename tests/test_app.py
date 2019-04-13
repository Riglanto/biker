import json
import pytest

from app import app


@pytest.fixture
def client():
    yield app.app.test_client()


def test_get_bikes(client):
    res = client.get('/bikes/stdev')
    data = json.loads(res.get_data(as_text=True))
    assert 'stdev' in data
