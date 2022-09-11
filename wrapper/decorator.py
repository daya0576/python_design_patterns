from wrapper.beverage import Beverage


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage


class Soy(CondimentDecorator):
    def cost(self) -> float:
        return self.beverage.cost() + 2.0


class Whip(CondimentDecorator):
    def cost(self) -> float:
        return self.beverage.cost() + 1.0


class Large(CondimentDecorator):
    def cost(self) -> float:
        return self.beverage.cost() + 1.5
