import logging

from circuits import Event

class log(Event):
    def __init__(self, **kwargs):

        # crash core circuit: multiple values for keyword argument 'name'
        kwargs['logger_name'] = kwargs['name']
        del(kwargs['name'])

        super().__init__(**kwargs)


class EventHandler(logging.Handler):
    def __init__(self, circuits):
        super().__init__()
        self.circuits = circuits

    def emit(self, record):
        infos = record.__dict__

        # event debug: infinite loop
        if infos['levelname'] == 'DEBUG' and \
                infos['filename'] == 'manager.py' and \
                infos['funcName'] == '_dispatcher':
            return

        self.circuits.fire(log(**infos))

