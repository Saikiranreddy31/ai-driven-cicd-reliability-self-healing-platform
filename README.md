🚀 AI-Driven CI/CD Reliability & Self-Healing Platform

An AI-powered CI/CD reliability engineering platform that detects application and infrastructure failures, analyzes root causes using AI, and performs automated self-healing actions with observability, gated deployments, and rollback support.

This project simulates real-world production reliability systems, not a toy demo.
Failures are intentionally injected, observed via metrics, alerted through SLOs, analyzed by AI, and automatically remediated.

🎯 Why This Project Exists

Modern DevOps is no longer about just deploying code.
It’s about keeping systems reliable under failure.

This project demonstrates:

Observability-first system design

SLO-driven alerting

CI-gated Continuous Deployment

Automated rollback on failure

Alert-driven self-healing

AI-assisted incident analysis & remediation decisions


Complete System Design

                         ┌───────────────────────────┐
                         │       GitHub Actions      │
                         │  CI + Gated CD Pipelines  │
                         └─────────────┬─────────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────────┐
│                        Production Platform                         │
│                                                                  │
│  ┌──────────────┐     /metrics     ┌──────────────┐             │
│  │  Sample App  │ ───────────────▶ │  Prometheus  │             │
│  │  (FastAPI)   │                  │  (Metrics)   │             │
│  │              │                  └──────┬───────┘             │
│  │  Failure     │                         │                     │
│  │  Injection   │                         ▼                     │
│  │  (latency,   │                  ┌──────────────┐             │
│  │  crash, 500) │                  │   Grafana    │             │
│  └──────┬───────┘                  │ Dashboards   │             │
│         │                            └──────────────┘             │
│         │                                                         │
│         │ SLO breach                                              │
│         ▼                                                         │
│  ┌──────────────┐     Webhook     ┌──────────────────────────┐   │
│  │ Alertmanager │ ──────────────▶ │      Self-Healer         │   │
│  │              │                 │  (FastAPI Service)       │   │
│  └──────────────┘                 │                          │   │
│                                   │  ┌────────────────────┐  │   │
│                                   │  │ AI Analyzer        │  │   │
│                                   │  │ (OpenAI API)       │  │   │
│                                   │  └─────────┬──────────┘  │   │
│                                   │            │             │   │
│                                   │   Decision │             │   │
│                                   │  (restart / no-op)       │   │
│                                   │            ▼             │   │
│                                   │  ┌────────────────────┐  │   │
│                                   │  │ Healing Engine     │  │   │
│                                   │  │ (Docker SDK)       │  │   │
│                                   │  └─────────┬──────────┘  │   │
│                                   │            │             │   │
│                                   └────────────┼─────────────┘   │
│                                                │                 │
│                                        Container Restart          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘



🔁 How AI Changes the System
❌ Traditional Alerting

Alert fires

Static rule → restart container

No context, no reasoning

✅ AI-Assisted Reliability (This Project)

Alert fires due to SLO breach

Alert payload sent to Self-Healer

AI analyzes:

Incident type

Probable root cause

Severity

Recommended action

Healing engine acts only if AI approves

Prevents unnecessary restarts

Creates explainable remediation

This mirrors modern SRE decision-making, not blind automation.


📦 Tech Stack

Python (FastAPI) – sample app & self-healer

Prometheus – metrics & recording rules

Grafana – dashboards

Alertmanager – alert routing

Docker & Docker Compose – orchestration

GitHub Actions – CI & CD pipelines

OpenAI API – AI-based incident analysis


🚀 Phase-Wise Implementation
✅ Phase 1 — Sample Service & Failure Injection

Built:

FastAPI service with:

/ping

/health

/metrics

Failure modes (via FAIL_MODE):

latency

crash

error

memory

Why:
Reliability engineering starts by expecting failure.

✅ Phase 2 — Dockerization

Dockerized the application

Standardized runtime with Uvicorn

Ensured parity between local & container execution

✅ Phase 3 — Observability & SLOs
Metrics

Request count

Latency histograms

Prometheus

Docker-based service discovery

Recording rules

Grafana

RPS dashboards

P95 latency

Availability

Alerting

SLO-based alerts

Alertmanager routing

🧪 Failure Testing
docker run -e FAIL_MODE=crash -p 8000:8000 infra-sample_app


Observed:

🚨 Alert fired

📉 Grafana spike

📨 Alertmanager received alert

✅ Phase 4 — Continuous Integration (CI)

GitHub Actions CI

Validates every commit

Prevents broken merges

✅ Phase 5 — Automated Self-Healing

Self-Healer service listens to alerts

Uses Docker SDK to restart containers

Fully automated recovery

♻️ Restarted container: sample_app

✅ Phase 6 — AI-Assisted Incident Analysis

Integrated OpenAI API

AI returns:

Root cause

Severity

Recommended action

Enum-based healing decisions

Result:
Smart, explainable remediation.

✅ Phase 7 — Gated CD, Health Checks & Rollback

CD runs only if CI is green

Docker health checks added

Automatic rollback on failure

This is production-grade CD, not basic deployment.

✅ Phase 8 — Production Readiness & Finalization

End-to-end validation

Crash → alert → AI → heal → recover

Stable release tagged

git tag v1.0-prod
