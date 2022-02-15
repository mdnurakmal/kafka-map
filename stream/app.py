from kafka import KafkaProducer
from confluent_kafka.admin import AdminClient, NewTopic
KAFKA_IP = os.getenv('KAFKA_IP', 'localhost')
KAFKA_PORT = os.getenv('KAFKA_PORT', '9092')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'car_data')



admin_client = AdminClient({
    "bootstrap.servers": KAFKA_IP+':'+KAFKA_PORT
})

topic_list = []
topic_list.append(NewTopic(KAFKA_TOPIC, 1, 1))
admin_client.create_topics(topic_list)




producer = KafkaProducer(bootstrap_servers=KAFKA_IP+':'+KAFKA_PORT)
producer.send(KAFKA_TOPIC, b'Hello, World!')
producer.send(KAFKA_TOPIC, key=b'message-two', value=b'This is Kafka-Python')