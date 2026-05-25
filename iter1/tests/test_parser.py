import pytest
from config.parser import parse_config

def test_valid():
    assert parse_config({})["timeout"] == 30

def test_invalid_timeout():
    with pytest.raises(ValueError):
        parse_config({"timeout": -1})

# iteration 1
