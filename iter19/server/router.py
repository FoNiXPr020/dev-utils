"""Route registry."""
from server.health import healthz

ROUTES = {
    "/healthz": healthz,
}

def dispatch(path, request):
    handler = ROUTES.get(path)
    if not handler:
        return {"error": "not found"}, 404
    return handler(request), 200

# iteration 19
