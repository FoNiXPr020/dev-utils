"""Configuration parser with input validation."""

from config.errors import ConfigValidationError


DEFAULTS = {
    "timeout": 30,
    "retries": 3,
    "port": 8080,
}


def validate_config(cfg: dict) -> None:
    """Raise ConfigValidationError if cfg contains invalid values."""
    if not isinstance(cfg.get("timeout"), (int, float)) or cfg["timeout"] <= 0:
        raise ConfigValidationError("timeout must be a positive number")
    if not isinstance(cfg.get("port"), int) or not (1 <= cfg["port"] <= 65535):
        raise ConfigValidationError("port must be an integer between 1 and 65535")
    if not isinstance(cfg.get("retries"), int) or cfg["retries"] < 0:
        raise ConfigValidationError("retries must be a non-negative integer")


def parse_config(raw: dict) -> dict:
    """Merge raw config over defaults and validate."""
    cfg = {**DEFAULTS, **raw}
    validate_config(cfg)
    return cfg
