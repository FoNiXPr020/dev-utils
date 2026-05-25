import time
from cache import Cache

def test_hit():
    c = Cache(ttl=60)
    c.set("k", "v")
    assert c.get("k") == "v"

def test_expired():
    c = Cache(ttl=0)
    c.set("k", "v")
    time.sleep(0.01)
    assert c.get("k") is None

# iteration 7
