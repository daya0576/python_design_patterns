from abc import ABC, abstractmethod

from observers.lifecycle import EventType, LifecycleEvent


class LifecycleListener(ABC):
    @abstractmethod
    def lifecycle_event(self, event: LifecycleEvent) -> None:
        ...


class FooLifecycleListener(LifecycleListener):
    def lifecycle_event(self, event: LifecycleEvent) -> None:
        if event.event_type is not EventType.START_EVENT:
            return None

        print("Foo event fired...")


class BarLifecycleListener(LifecycleListener):
    def lifecycle_event(self, event: LifecycleEvent) -> None:
        if event.event_type is not EventType.STOP_EVENT:
            return None

        print("Bar event fired...")
