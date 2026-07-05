"""Test configuration for Prospect Research Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "prospect-research-agent", "category": "Sales"}
