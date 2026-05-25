"""TTL in-memory cache."""
import time

class Cache:
    def __init__(self, ttl=300):
        self._ttl = ttl
        self._data = {}

    def get(self, key):
        entry = self._data.get(key)
        if entry and time.time() < entry["exp"]:
            return entry["val"]
        return None

    def set(self, key, val):
        self._data[key] = {"val": val, "exp": time.time() + self._ttl}

# iteration 27
