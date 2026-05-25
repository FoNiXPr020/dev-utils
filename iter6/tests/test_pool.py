from unittest.mock import MagicMock
from db.pool import Pool

def test_stale_conn_recycled():
    bad = MagicMock()
    bad.ping.side_effect = Exception("stale")
    good = MagicMock()
    pool = Pool(lambda: good, size=0)
    pool._conns = [bad]
    conn = pool.get()
    assert conn is good

# iteration 6
