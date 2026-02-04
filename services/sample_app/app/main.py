from fastapi import FastAPI
import time
import logging

from app.failures import maybe_fail
from app.metrics import REQUEST_COUNT, REQUEST_LATENCY

app = FastAPI(title="Failing Reliability Service")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sample_app")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ping")
def ping():
    start = time.time()

    maybe_fail()

    latency = time.time() - start
    REQUEST_LATENCY.observe(latency)
    REQUEST_COUNT.inc()

    logger.info("Ping success", extra={"latency": latency})
    return {"message": "pong", "latency": latency}
