from app import bikes

def test_stdev():
	result = bikes.stdev()
	assert 'stdev' in result