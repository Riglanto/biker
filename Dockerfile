FROM ubuntu:16.04
LABEL maintainer="R"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
	pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]