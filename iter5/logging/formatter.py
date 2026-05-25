"""JSON log formatter."""
import json, logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({"level": record.levelname, "msg": record.getMessage(), "name": record.name})

# iteration 5
