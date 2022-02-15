from kafka import KafkaProducer

import os

from confluent_kafka.admin import AdminClient, NewTopic

KAFKA_IP = os.getenv('KAFKA_IP')
KAFKA_PORT = os.getenv('KAFKA_PORT')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')

print(KAFKA_IP+':'+KAFKA_PORT)

admin_client = AdminClient({
    "bootstrap.servers": KAFKA_IP+':'+KAFKA_PORT
})

topic_list = []
topic_list.append(NewTopic(KAFKA_TOPIC, 1, 1))
admin_client.create_topics(topic_list)

print(KAFKA_IP+':'+KAFKA_PORT)
producer = KafkaProducer(bootstrap_servers=KAFKA_IP+':'+KAFKA_PORT)
producer.send(KAFKA_TOPIC, b'Hello, World!')
producer.send(KAFKA_TOPIC, key=b'message-two', value=b'This is Kafka-Python')