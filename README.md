# Original Repository
https://github.com/code-and-dogs/liveMaps

## Fresh VM
```
sudo apt-get update -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo apt install docker-compose -y
git clone https://github.com/mdnurakmal/kafka-map.git
```
## Run script
```
sudo sh run_docker.sh
```
## View exited containers
docker ps -a | grep Exit

## Open kowl browser
<publicIP>:8080

## Bash into container
sudo docker exec -it <mycontainer> /bin/bash

## run a temp container
```
sudo docker run -it curlimages/curl /bin/sh
```
or
```
sudo docker-compose run temp kowl:8080
```
/opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic car_data --from-beginning

