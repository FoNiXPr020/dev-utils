from events import bus

def test_pubsub():
    received = []
    bus.subscribe("test", received.append)
    bus.publish("test", {"x": 1})
    assert received == [{"x": 1}]

# iteration 10
