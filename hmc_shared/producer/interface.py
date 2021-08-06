from hmc_shared.utils import RabbitmqHandler
import requests


class ProducerKinds:
    DIVAR = 'divar'
    BAMA = 'bama'
    SHEYPOOR = 'sheypoor'


class Producer:
    def __init__(self, *args, **kwargs):
        self.kind = kwargs.get('kind')
        rabbitmq_host = kwargs.get('rabbitmq_host')
        rabbitmq_port = kwargs.get('rabbitmq_port')
        self.rabbitmq_handler = RabbitmqHandler(
            rabbitmq_host=rabbitmq_host,
            rabbitmq_port=rabbitmq_port
        )

    def produce(self, *args, **kwargs):
        raise NotImplementedError

    def get_next_batch(self, *args, **kwargs):
        raise NotImplementedError

    def request(self, url):
        pass

    def generate_next_url(self):
        raise NotImplementedError

    def push_to_queue(self, data):
        self.rabbitmq_handler.push(
            routing_key=self.kind,
            data=data
        )
