import os
import random
import time
import sys

FAIL_MODE = os.getenv("FAIL_MODE", "none")


def maybe_fail():
    if FAIL_MODE == "crash":
        if random.random() < 0.3:
            sys.exit("💥 Simulated crash")

    elif FAIL_MODE == "latency":
        time.sleep(random.randint(2, 6))

    elif FAIL_MODE == "error":
        raise Exception("🔥 Simulated 500 error")

    elif FAIL_MODE == "memory":
        leak = []
        for _ in range(5000):
            leak.append("leak" * 1000)

