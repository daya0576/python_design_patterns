from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any


class Lifecycle(ABC):
    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...


class EventType(Enum):
    START_EVENT = "start"
    STOP_EVENT = "stop"


@dataclass
class LifecycleEvent:
    lifecycle: Lifecycle
    event_type: EventType
    data: Any
