import unittest
from observers.events import BarLifecycleListener, FooLifecycleListener

from observers.pipeline import SimplePipeline


class TestPipeline(unittest.TestCase):
    def test_events(self):
        pipeline = SimplePipeline()
        pipeline.add_listener(FooLifecycleListener())
        pipeline.add_listener(BarLifecycleListener())

        pipeline.process()
