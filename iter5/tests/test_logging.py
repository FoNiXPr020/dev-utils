import json
from logging.setup import get_logger

def test_json_output(capsys):
    log = get_logger("test")
    log.warning("hello")
    out = capsys.readouterr().err
    data = json.loads(out.strip())
    assert data["level"] == "WARNING"

# iteration 5
