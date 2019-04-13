from unittest.mock import patch
import pytest
import os

from app import bikes

NON_EXISTING_CSV_PATH = os.path.join('non_existing.csv')

def test_load_data():
	data = bikes.load_data()
	assert len(data) == 17379

@patch('os.path.join')
def test_load_data_missing_file(mock_data_path):
	mock_data_path.return_value = NON_EXISTING_CSV_PATH
	with pytest.raises(FileNotFoundError) as excinfo:
		bikes.load_data()

def test_stdev():
	result = bikes.stdev()

	assert 'stdev' in result
	stdev = result['stdev']

	assert 'casual' in stdev
	casual = stdev['casual']
	assert len(casual) == 7
	assert casual['Mon'] == 809.324777013928
	assert casual['Sun'] == 927.0828839032538 

	assert 'registered' in stdev
	registered = stdev['registered']
	assert len(registered) == 7
	assert registered['Mon'] == 1179.713036054064
	assert registered['Sun'] == 1358.0687837619162