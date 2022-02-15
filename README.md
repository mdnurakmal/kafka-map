# kafka-map
## Run script
sudo sh run_docker.sh

## View exited containers
docker ps -a | grep Exit

## Open kowl browser
<publicIP>:8080

## Bash into container
sudo docker exec -it <mycontainer> /bin/bash

/opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic car_data --from-beginning

