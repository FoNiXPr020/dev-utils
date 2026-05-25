"""Generic retry utility with exponential backoff."""

import time
import logging
from typing import Callable, Type, Tuple

log = logging.getLogger(__name__)


def with_retry(
    fn: Callable,
    attempts: int = 3,
    backoff: float = 1.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
):
    """Call fn, retrying on specified exceptions with exponential backoff.

    Args:
        fn:         Zero-argument callable to invoke.
        attempts:   Maximum number of attempts.
        backoff:    Base backoff in seconds (doubles each retry).
        exceptions: Exception types that trigger a retry.

    Returns:
        Return value of fn on success.

    Raises:
        The last exception raised by fn after all attempts are exhausted.
    """
    last_exc = None
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except exceptions as exc:
            last_exc = exc
            if attempt < attempts:
                wait = backoff * (2 ** (attempt - 1))
                log.warning(
                    "Attempt %d/%d failed (%s). Retrying in %.1fs...",
                    attempt, attempts, exc, wait
                )
                time.sleep(wait)
    raise last_exc
