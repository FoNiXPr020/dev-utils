"""Retry with exponential backoff."""
import time, logging
log = logging.getLogger(__name__)

def with_retry(fn, attempts=3, backoff=1.0):
    for i in range(1, attempts + 1):
        try:
            return fn()
        except Exception as e:
            if i == attempts:
                raise
            time.sleep(backoff * 2 ** (i - 1))

# iteration 2
