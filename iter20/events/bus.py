"""Simple synchronous event bus."""
from collections import defaultdict

class EventBus:
    def __init__(self):
        self._handlers = defaultdict(list)

    def subscribe(self, event, fn):
        self._handlers[event].append(fn)

    def publish(self, event, payload=None):
        for fn in self._handlers[event]:
            fn(payload)

# iteration 20
