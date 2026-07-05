"""Prospect Research Agent - MCP Server."""

import structlog

logger = structlog.get_logger(__name__)


class MCPServer:
    """MCP server for Prospect Research Agent."""

    def __init__(self):
        logger.info("mcp_server_initialized")
