from flask import Flask, render_template, Response
from confluent_kafka import Consumer

import os

KAFKA_IP = os.getenv('KAFKA_IP')
KAFKA_PORT = os.getenv('KAFKA_PORT')

c = Consumer({
    'bootstrap.servers': KAFKA_IP+":"+KAFKA_PORT,
    'group.id': 'mygroup',
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
    def events():
        yield 'data:{0}\n\n'.format(msg.value().decode('utf-8'))

    msg = c.poll(1.0)

    if msg is None:
        print("None")
    else:
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
        else:
            print('Received message: {}'.format(msg.value().decode('utf-8')))
            return Response(events(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')