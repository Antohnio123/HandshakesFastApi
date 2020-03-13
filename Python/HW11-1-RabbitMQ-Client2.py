import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='numbers')


def callback(ch, method, properties, body):
    print('Received: {}'.format(body.decode()))
    with open('log2.txt', 'a') as logfile:
        logfile.write('Received {}: {}\n'.format(datetime.datetime.now(), body.decode()))


channel.basic_consume('numbers', callback,  auto_ack=True)


print('Waiting for other messages. To close press Ctrl+Break')
channel.start_consuming()
