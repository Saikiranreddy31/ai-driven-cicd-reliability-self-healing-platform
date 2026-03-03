# 🚀 AI-Driven CI/CD Reliability & Self-Healing Platform

A production-style reliability engineering platform that detects CI/CD and application failures using observability signals, triggers automated remediation workflows, and validates recovery through metrics and health checks.

This project simulates real-world Site Reliability Engineering practices: failure injection, SLO-based alerting, automated recovery, and gated deployments.

---

## 🎯 Key Capabilities

- Prometheus-based anomaly detection  
- SLO-driven alerting  
- CI-gated Continuous Deployment  
- Automated rollback on failure  
- Alert-triggered self-healing  
- Failure simulation & resilience testing  

---

## 🛠 Tech Stack

- Python (FastAPI)  
- Prometheus  
- Grafana  
- Alertmanager  
- Docker & Docker Compose  
- GitHub Actions  

---

## 🏗️ System Overview

CI Pipeline → Containerized Service → Metrics → Alerting → Recovery Engine

1. GitHub Actions validates every commit  
2. Dockerized FastAPI service exposes Prometheus metrics  
3. Prometheus evaluates latency and error thresholds  
4. Alertmanager routes SLO breaches  
5. Recovery service executes automated remediation  
6. Health checks verify service restoration  

---

## 🔎 Failure Scenarios Simulated

Controlled failures are injected to validate reliability mechanisms:

- Latency spikes  
- Container crashes  
- HTTP 500 errors  
- Deployment failures  

Each failure triggers:

- Metric deviation  
- Alert generation  
- Automated recovery workflow  
- Post-recovery validation  

---

## 📊 Observability Stack

- Prometheus — metrics collection and recording rules  
- Grafana — dashboards (RPS, latency percentiles, availability)  
- Alertmanager — SLO-based alert routing  

---

## 🔁 Automated Recovery Workflow

When an SLO breach occurs:

1. Alert is triggered  
2. Recovery service receives webhook  
3. Failure context is analyzed  
4. Remediation action is executed (container restart or rollback)  
5. Service health is validated  

This reduces manual intervention during simulated outages.

---

## 🔄 CI/CD Pipeline

- GitHub Actions for Continuous Integration  
- Deployment only if CI passes  
- Docker health checks  
- Automatic rollback on unhealthy release  

---

## 🧠 AI-Assisted Incident Analysis

An AI module analyzes alert payloads and suggests remediation decisions, enabling explainable recovery workflows.

---

## 🧪 Example Failure Test

```bash
docker run -e FAIL_MODE=crash -p 8000:8000 sample_app
```

Expected behavior:

- Alert fires  
- Recovery is triggered  
- Container restarts  
- Service restores successfully  

---

## 🏷️ Stable Release

v1.0-prod
