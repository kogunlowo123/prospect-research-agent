# Prospect Research Agent

[![CI](https://github.com/kogunlowo123/prospect-research-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/prospect-research-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Sales | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Prospect research agent that compiles company profiles, identifies key decision-makers, tracks buying signals, analyzes competitive landscape, and generates pre-call briefings for sales reps.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `research_company` | Compile comprehensive company research profile |
| `identify_stakeholders` | Identify key decision-makers and influencers at a target account |
| `track_buying_signals` | Track intent and buying signals from a prospect |
| `analyze_competitors` | Analyze competitive landscape for a prospect account |
| `generate_briefing` | Generate a pre-call research briefing for a sales rep |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/prospect-research/execute` | Execute primary action |
| `POST` | `/api/v1/prospect-research/analyze` | Run analysis |
| `GET` | `/api/v1/prospect-research/metrics` | Get metrics |
| `PUT` | `/api/v1/prospect-research/configure` | Configure settings |
| `POST` | `/api/v1/prospect-research/report` | Generate report |

## Features

- Prospect
- Research
- Analytics
- Automation

## Integrations

- Salesforce
- Hubspot
- Outreach
- Apollo
- Linkedin Sales Navigator

## Architecture

```
prospect-research-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── prospect_research_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CRM + Sales Engagement + LLM**

---

Built as part of the Enterprise AI Agent Platform.
