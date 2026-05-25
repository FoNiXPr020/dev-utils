"""Sliding window rate limiter."""
import time
from collections import deque

class RateLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self._calls = deque()

    def allow(self):
        now = time.time()
        while self._calls and self._calls[0] < now - self.window:
            self._calls.popleft()
        if len(self._calls) < self.limit:
            self._calls.append(now)
            return True
        return False

# iteration 28
