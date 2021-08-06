from hmc_shared.utils import RabbitmqHandler


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

    def request(self, *args, **kwargs):
        raise NotImplementedError

    def prepare_next_request(self, *args, **kwargs):
        raise NotImplementedError

    def push_to_queue(self, data):
        self.rabbitmq_handler.push(
            routing_key=self.kind,
            data=data
        )

    @staticmethod
    def prepare_data(last_response):
        raise NotImplementedError
