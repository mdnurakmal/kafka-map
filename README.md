# kafka-map

Bash into container
sudo docker exec -it <mycontainer> /bin/bash

/opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic car_data --from-beginning

/opt/bitnami/kafka/bin/kafka-console-consumer.sh --new-consumer --bootstrap-server localhost:9092 --topic car_data --from-beginning