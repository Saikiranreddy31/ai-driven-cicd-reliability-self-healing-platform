# ai-driven-cicd-reliability-self-healing-platform
An AI-driven CI/CD reliability engineering platform that detects pipeline and infrastructure failures, analyzes root causes, and performs automated self-healing actions with observability and rollback support.

This project is a hands-on SRE / DevOps system built to simulate real-world reliability problems and show how modern teams observe, alert, and respond to failures.

Instead of a toy app, this setup behaves like a real production service: it exposes metrics, fails in controlled ways, triggers alerts, and visualizes everything through dashboards. The next step is to make it self-healing.

🎯 What I’m Building (and Why)

The goal of this project is to understand and demonstrate how reliability is handled in real systems, not just how apps are deployed.


This project focuses on:

Building a production-like microservice

Adding metrics from day one

Monitoring the service using Prometheus

Visualizing system health in Grafana

Defining SLOs and error budgets

Triggering alerts when things go wrong

(Next) Automatically fixing issues using self-healing automation

🧱 High-Level Architecture
┌────────────┐
│ Sample App │  (FastAPI + Failure Injection)
└─────┬──────┘
      │ /metrics
┌─────▼────────┐
│ Prometheus   │  (Metrics scraping & recording rules)
└─────┬────────┘
      │
┌─────▼────────┐
│ Grafana      │  (Dashboards & visualization)
└─────┬────────┘
      │
┌─────▼────────┐
│ Alertmanager │  (SLO-based alerts)
└──────────────┘

📦 Tech Stack

Python (FastAPI) – service implementation

Prometheus – metrics collection & rules

Grafana – dashboards and visualization

Alertmanager – alert routing

Docker & Docker Compose – containerization

Failure Injection (Chaos) – controlled outages

GitHub Actions (Phase 4) – CI/CD & automation

🚀 Phase-Wise Implementation
✅ Phase 1 — Sample Service & Failure Injection

What I built:

A FastAPI service with:

/ping

/health

/metrics

Built-in failure modes:

latency (slow responses)

crash (process exits)

error (500 errors)

memory (simulated memory leak)

Failures are controlled using an environment variable: FAIL_MODE

Why this matters:

Real reliability work starts by expecting failures, not avoiding them.

✅ Phase 2 — Dockerization

What I did:

Dockerized the application

Standardized runtime using Uvicorn

Verified the app runs the same locally and inside Docker

Outcome:

The service is now portable, reproducible, and production-ready.

✅ Phase 3 — Observability & Reliability Engineering
🔹 Phase 3.1 — Metrics Instrumentation

Added custom Prometheus metrics:

Request count

Request latency (histograms)

🔹 Phase 3.2 — Prometheus Setup

Configured Prometheus scraping

Docker-based service discovery

Verified targets and metrics ingestion

🔹 Phase 3.3 — Grafana Dashboards

Created and provisioned dashboards for:

Request rate (RPS)

Latency (P95)

Service availability

🔹 Phase 3.4 — SLOs & Alerting

Defined recording rules:

sample_app:request_rate

sample_app:latency_p95

sample_app:availability

Configured Alertmanager

Alerts fire automatically when SLOs are breached

Verified end-to-end:

Prometheus shows alert states

Grafana reflects real-time spikes

Alertmanager receives and manages alerts

🧪 Failure Testing

Run the service with failures enabled:

docker run -e FAIL_MODE=latency -p 8000:8000 failing-service


or:

docker run -e FAIL_MODE=crash -p 8000:8000 failing-service


What you’ll see:

🚨 Alerts firing in Prometheus

📉 Latency spikes in Grafana

📊 Dashboards updating in real time

🏁 Current Status

✔ Phase 1 — Completed

✔ Phase 2 — Completed

✔ Phase 3 — Completed