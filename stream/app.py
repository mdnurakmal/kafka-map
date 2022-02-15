from kafka import KafkaProducer

import os

from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

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

p = Producer({'bootstrap.servers': KAFKA_IP+':'+KAFKA_PORT})
p.produce('mytopic', "test", callback=delivery_report)
p.flush()
