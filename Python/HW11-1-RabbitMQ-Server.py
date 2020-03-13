import pika

D =['кошка', 'собака', 'слон', 'птица', 'рыба', 'волк', 'змея']
N = 5
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='animals', durable = False)
channel.queue_declare(queue='numbers', durable = False)

for i in range(7):
    channel.basic_publish(exchange='', routing_key= 'animals', body=(D[i]).encode(),
                          properties = pika.BasicProperties(delivery_mode=2))
    channel.basic_publish(exchange='', routing_key= 'numbers', body=(str(N*i)).encode(),
                          properties = pika.BasicProperties(delivery_mode=2))

print ('Two blocks of messages have been sent')