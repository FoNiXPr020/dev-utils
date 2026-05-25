# Utility Modules

## `utils.retry.with_retry`

Wraps any zero-argument callable with configurable retry and exponential backoff.

### Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fn` | `Callable` | — | Function to call |
| `attempts` | `int` | `3` | Max attempts |
| `backoff` | `float` | `1.0` | Base backoff in seconds |
| `exceptions` | `tuple` | `(Exception,)` | Exceptions that trigger retry |

### Example

```python
from utils import with_retry

result = with_retry(
    fn=lambda: requests.get('https://api.example.com/data'),
    attempts=4,
    backoff=0.5,
    exceptions=(requests.ConnectionError, requests.Timeout),
)
```
