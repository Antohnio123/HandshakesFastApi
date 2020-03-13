import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='animals')


def callback(ch, method, properties, body):
    print('Received: {}'.format(body.decode()))
    with open('log1.txt', 'a') as logfile:
        logfile.write('Received {}: {}\n'.format(datetime.datetime.now(), body.decode()))

channel.basic_consume('animals', callback,  auto_ack=True)


print('Waiting for other messages. To close press Ctrl+Break')
channel.start_consuming()


