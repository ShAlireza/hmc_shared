class Producer:

    def produce(self, *args, **kwargs):
        raise NotImplementedError

    def push_to_queue(self):
        pass

    def get_next_batch(self):
        raise NotImplementedError
