"""Logger factory."""
import logging
from logging.formatter import JsonFormatter

def get_logger(name):
    h = logging.StreamHandler()
    h.setFormatter(JsonFormatter())
    log = logging.getLogger(name)
    log.addHandler(h)
    return log

# iteration 15
