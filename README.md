# Biker - the proper take-home interview task

Build and start docker
```
docker build -t biker .
docker run -p 80:8000 biker
```

Run curl against docker container
```
curl localhost/bikes/stdev
```

Run tests
```
python -m pytest
```

In case you haven't cleaned up for some time:
```
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```

Or connect to container:
```
docker exec -it <container_id> /bin/bash
````
