from flask import Flask, render_template, Response
from confluent_kafka import Consumer

import os

KAFKA_IP = os.getenv('KAFKA_IP')
KAFKA_PORT = os.getenv('KAFKA_PORT')

c = Consumer({
    'bootstrap.servers': 'kafka1',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['mytopic'])

def get_kafka_client():
    return KafkaClient(hosts=KAFKA_IP+':'+KAFKA_PORT)

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

#Consumer API
@app.route('/topic/<topicname>')
def get_messages(topicname):
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))
    # client = get_kafka_client()
    # def events():
    #     for i in client.topics[topicname].get_simple_consumer():
    #         yield 'data:{0}\n\n'.format(i.value.decode())
    # return Response(events(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')