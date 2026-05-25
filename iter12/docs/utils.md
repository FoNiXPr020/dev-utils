# Utils

## with_retry

Retries a callable with exponential backoff.

```python
from utils import with_retry
result = with_retry(lambda: fetch_data(), attempts=4)
```

# iteration 12
