from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "sample_app_requests_total",
    "Total HTTP requests"
)

REQUEST_LATENCY = Histogram(
    "sample_app_request_latency_seconds",
    "Request latency"
)
