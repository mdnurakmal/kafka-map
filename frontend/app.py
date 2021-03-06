from flask import Flask, render_template, Response
from confluent_kafka import Consumer

import os
import time
time.sleep(10)   # Delays for 5 seconds. You can also use a float value.

KAFKA_IP = os.getenv('KAFKA_IP')
KAFKA_PORT = os.getenv('KAFKA_PORT')
print(KAFKA_IP)
c = Consumer({
    'bootstrap.servers': KAFKA_IP+":"+KAFKA_PORT,
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['mytopic'])

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

#Consumer API
@app.route('/topic/<topicname>')
def get_messages(topicname):

    msg = c.poll(1.0)

    if msg is None:
        print("None")
    else:
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
        else:
            print('Received message: {}'.format(msg.value().decode('utf-8')))
            return Response('data:{0}\n\n'.format(msg.value().decode('utf-8')), mimetype="text/event-stream")
    
    return Response('data:{0}\n\n'.format(""), mimetype="text/event-stream")

def main():
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        c.close()


if __name__ == '__main__':
    main()

