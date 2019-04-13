# # Backend Interview

# We are thrilled you are interviewing with us! The goal of this project is to see how you think, how you prioritize tasks when there is a lot to do and how quickly you can pick up new coding concepts. This project is as much for us as it is for you, we want you to get a sense of what working with us is like. Don't be afraid to ask questions!

# 1. Please download the hour.csv from https://archive.ics.uci.edu/ml/machine-learning-databases/00275/

# 2. Please build an API (Flask/Django) with a Nginx/Gunicorn server in docker
#    - Build one endpoint where you return the standard deviation in bike rentals (for registered and casual users separately) for every weekday (i.e. Monday, Tuesday, Wednesday, Thursday, Friday) (using parallel processing)
#    - Please implement best practices TDD/BDD and https://www.python.org/dev/peps/pep-0008/

# 3. Please provide instructions on how the docker can be started and how the API will be accessed.

def stdev():
	return {'stdev' : {}}