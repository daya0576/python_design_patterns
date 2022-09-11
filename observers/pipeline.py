from abc import ABC, abstractmethod
from observers.events import LifecycleListener
from observers.lifecycle import EventType, Lifecycle
from observers.utils import LifecycleSupport


class BasePipeline(Lifecycle, ABC):
    def __init__(self):
        self.lifecycle = LifecycleSupport(self)

    @abstractmethod
    def _do_load_data(self):
        ...

    @abstractmethod
    def _do_process(self):
        ...

    def start(self):
        self.lifecycle.fire_lifecycle_listener(EventType.START_EVENT)

    def stop(self):
        self.lifecycle.fire_lifecycle_listener(EventType.STOP_EVENT)

    def add_listener(self, listener: LifecycleListener):
        self.lifecycle.add_lifecycle_listener(listener)

    def process(self):
        print("Start..")
        self.start()
        self._do_load_data()
        self._do_process()
        self.stop()
        print("Stop")


class SimplePipeline(BasePipeline):
    def _do_load_data(self):
        print("Do load data")

    def _do_process(self):
        print("Do process")
