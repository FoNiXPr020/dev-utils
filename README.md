# dev-utils

A collection of developer utilities for config parsing, retry logic, and CLI tooling.

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Copy `.env.example` to `.env` and fill in values before running.

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `APP_SECRET_KEY` | ✅ | — | Secret key for signing tokens |
| `DB_POOL_SIZE` | ❌ | `5` | Number of DB connections in pool |
| `CACHE_TTL_SECONDS` | ❌ | `300` | Cache entry lifetime in seconds |
| `LOG_LEVEL` | ❌ | `INFO` | Logging verbosity (`DEBUG`, `INFO`, `WARNING`) |
| `API_BASE_URL` | ✅ | — | Base URL for outbound API calls |

## Usage

```python
from config.parser import parse_config
from utils import with_retry
```

## Contributing

Please open an issue before submitting a PR. Run `pytest` before pushing.
