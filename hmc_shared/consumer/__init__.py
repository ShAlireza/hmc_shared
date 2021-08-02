from hmc_shared.utils import RabbitmqHandler


class Consumer:
    def __init__(self, *args, **kwargs):
        self.kind = kwargs.get('kind')
        rabbitmq_host = kwargs.get('rabbitmq_host')
        rabbitmq_port = kwargs.get('rabbitmq_port')
        self.rabbitmq_handler = RabbitmqHandler(
            rabbitmq_host=rabbitmq_host,
            rabbitmq_port=rabbitmq_port
        )
        self.start_consumer()

    def start_consumer(self):
        self.rabbitmq_handler.channel.basic_consume(
            queue=self.kind,
            on_message_callback=self.callback,
            auto_ack=False
        )
        self.rabbitmq_handler.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        self.process(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def process(self, data):
        raise NotImplementedError

