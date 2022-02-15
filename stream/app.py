from kafka import KafkaProducer

import os

from kafka.admin import KafkaAdminClient, NewTopic

print("Hello")
# KAFKA_IP = os.getenv('KAFKA_IP')
# KAFKA_PORT = os.getenv('KAFKA_PORT')
# KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')



# admin_client = KafkaAdminClient(
#     bootstrap_servers=KAFKA_IP+':'+KAFKA_PORT, 
#     client_id='test'
# )

# topic_list = []
# topic_list.append(NewTopic(name=KAFKA_TOPIC, num_partitions=1, replication_factor=1))
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

# print(KAFKA_IP+':'+KAFKA_PORT)
# producer = KafkaProducer(bootstrap_servers=KAFKA_IP+':'+KAFKA_PORT)
# producer.send(KAFKA_TOPIC, b'Hello, World!')
# producer.send(KAFKA_TOPIC, key=b'message-two', value=b'This is Kafka-Python')