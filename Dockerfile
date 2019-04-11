FROM ubuntu:18.04
LABEL maintainer="R"

RUN apt-get update -y && \
    apt-get install -y python3 python3-dev python3-pip

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]