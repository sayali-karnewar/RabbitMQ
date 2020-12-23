import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '5672', '/', pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()



channel.queue_declare(queue='queue3', durable=True)
channel.queue_bind(queue='queue3', routing_key='key1', exchange='my_exchange')
def callback(ch, method, properties, body):
    print(body, 'is recieved')

channel.basic_consume(queue='queue3', on_message_callback=callback, auto_ack = True)

channel.start_consuming()
