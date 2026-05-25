import pytest
from config.parser import parse_config
from config.errors import ConfigValidationError


def test_valid_config():
    cfg = parse_config({"timeout": 10, "port": 443, "retries": 2})
    assert cfg["timeout"] == 10


def test_negative_timeout_raises():
    with pytest.raises(ConfigValidationError, match='timeout'):
        parse_config({"timeout": -1})


def test_invalid_port_raises():
    with pytest.raises(ConfigValidationError, match='port'):
        parse_config({"port": 99999})


def test_defaults_applied():
    cfg = parse_config({})
    assert cfg["retries"] == 3
