from core import Log
from .EventHandler import EventHandler

from circuits import Component
import logging


class Module(Component):
    channel = 'log'

    def started(self, component):
        handler = EventHandler(self)
        Log.get_logger().addHandler(handler)

