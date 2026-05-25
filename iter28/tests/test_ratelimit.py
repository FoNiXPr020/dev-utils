from ratelimit.window import RateLimiter

def test_allows_up_to_limit():
    r = RateLimiter(3, 1)
    assert all(r.allow() for _ in range(3))
    assert not r.allow()

# iteration 28
