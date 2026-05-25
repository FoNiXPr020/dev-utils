"""DB connection pool with health checks."""

class Pool:
    def __init__(self, factory, size=5):
        self._factory = factory
        self._conns = [factory() for _ in range(size)]

    def get(self):
        conn = self._conns.pop()
        if not self._ping(conn):
            conn = self._factory()
        return conn

    def _ping(self, conn):
        try:
            conn.ping()
            return True
        except Exception:
            return False

# iteration 16
