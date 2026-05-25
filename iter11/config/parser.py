"""Config parser with validation."""

DEFAULTS = {"timeout": 30, "retries": 3, "port": 8080}

def parse_config(raw):
    cfg = {**DEFAULTS, **raw}
    if cfg["timeout"] <= 0:
        raise ValueError("timeout must be positive")
    return cfg

# iteration 11
