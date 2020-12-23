import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '5672', '/', pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()


channel.basic_publish(exchange='my_exchange', routing_key='key1', body='Test!!')
print("message sent :Hi from producer side")
channel.close()