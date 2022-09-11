from typing import Any, List

from observers.events import LifecycleListener
from observers.lifecycle import EventType, Lifecycle, LifecycleEvent


class LifecycleSupport:
    def __init__(self, lifecycle: Lifecycle):
        self._listeners: List[LifecycleListener] = []
        self._lifecycle = lifecycle

    def add_lifecycle_listener(self, listener: LifecycleListener):
        self._listeners.append(listener)

    def remove_lifecyle_listener(self, event: LifecycleEvent):
        self._listeners = [x for x in self._listeners if x != event]

    def fire_lifecycle_listener(self, event_type: EventType, data: Any = None):
        event = LifecycleEvent(self._lifecycle, event_type, data)
        for listener in self._listeners:
            listener.lifecycle_event(event)
