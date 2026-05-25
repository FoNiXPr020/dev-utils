"""Health check endpoint."""

def healthz(request):
    return {"status": "ok", "uptime": "running"}

# iteration 29
