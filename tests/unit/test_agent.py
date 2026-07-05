"""Prospect Research Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_research_company():
    """Test Compile comprehensive company research profile."""
    tools = AgentTools()
    result = await tools.research_company(company_name="test", data_points="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_identify_stakeholders():
    """Test Identify key decision-makers and influencers at a target account."""
    tools = AgentTools()
    result = await tools.identify_stakeholders(company_name="test", buying_center_roles="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_buying_signals():
    """Test Track intent and buying signals from a prospect."""
    tools = AgentTools()
    result = await tools.track_buying_signals(company_name="test", signal_sources="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_competitors():
    """Test Analyze competitive landscape for a prospect account."""
    tools = AgentTools()
    result = await tools.analyze_competitors(company_name="test", our_competitors="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.prospect_research_agent_agent import ProspectResearchAgentAgent
    agent = ProspectResearchAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
