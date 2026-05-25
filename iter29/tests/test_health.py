from server.router import dispatch

def test_healthz_ok():
    body, status = dispatch("/healthz", {})
    assert status == 200
    assert body["status"] == "ok"

# iteration 29
