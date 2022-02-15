from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic


KAFKA_IP = os.getenv('KAFKA_IP', 'localhost')
KAFKA_PORT = os.getenv('KAFKA_PORT', '9092')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'car_data')

admin_client = KafkaAdminClient(
    bootstrap_servers=KAFKA_IP+':'+KAFKA_PORT, 
    client_id='test'
)

topic_list = []
topic_list.append(NewTopic(name=KAFKA_TOPIC, num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)



producer = KafkaProducer(bootstrap_servers=KAFKA_IP+':'+KAFKA_PORT)
producer.send('sample', b'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')