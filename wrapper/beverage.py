from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float:
        ...


class Espresso(Beverage):
    def cost(self) -> float:
        return 12.0
