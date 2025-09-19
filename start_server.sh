#!/bin/bash
# AI Validation Server Startup Script

echo "🚀 Starting AI Validation MCP Server..."
cd "$(dirname "$0")"
python mcp_server.py
