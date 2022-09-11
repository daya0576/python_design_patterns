import unittest

from wrapper.beverage import Espresso
from wrapper.decorator import Large, Soy, Whip


class TestPipeline(unittest.TestCase):
    def test_mixed_beverage(self):
        beverage = Espresso()
        beverage = Large(Whip(Soy(beverage)))
        print(beverage.cost())
