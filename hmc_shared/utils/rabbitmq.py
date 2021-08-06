import json

import pika

__all__ = ('RabbitmqHandler',)


class RabbitmqHandler:

    def __init__(self, rabbitmq_host: str, rabbitmq_port: int):
        self.rabbitmq_host = rabbitmq_host
        self.rabbitmq_port = rabbitmq_port

        self.connection = self.create_connection()
        self.channel = self.create_channel()

    def push(self, routing_key, data):
        self.channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=json.dumps(data).encode('utf-8'),
            properties=pika.BasicProperties(
                delivery_mode=2  # make message persistent
            )
        )

    def pull(self, routing_key, callback_func):
        self.channel.basic_consume(
            queue=routing_key,
            on_message_callback=callback_func,
            auto_ack=False
        )
        self.channel.start_consuming()

    def create_connection(self):
        return pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host=self.rabbitmq_host,
                port=self.rabbitmq_port
            )
        )

    def create_channel(self):
        channel = self.connection.channel()
        channel.basic_qos(prefetch_count=1)

        return channel

    def close(self):
        self.channel.close()
        self.connection.close()
