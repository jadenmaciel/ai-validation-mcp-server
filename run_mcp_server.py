#!/usr/bin/env python3
"""
MCP Server Runner

This script runs the AI Validation MCP server using the virtual environment.
It's designed to be called from Cursor's mcp.json configuration.
"""

import os
import sys
import subprocess

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the virtual environment python
    venv_python = os.path.join(script_dir, "venv", "bin", "python")
    
    # Path to the MCP server script
    mcp_server_script = os.path.join(script_dir, "ai_validation_mcp.py")
    
    # Check if virtual environment exists
    if not os.path.exists(venv_python):
        print("Error: Virtual environment not found. Please run: python3 -m venv venv && source venv/bin/activate && pip install mcp", file=sys.stderr)
        sys.exit(1)
    
    # Check if MCP server script exists
    if not os.path.exists(mcp_server_script):
        print(f"Error: MCP server script not found at {mcp_server_script}", file=sys.stderr)
        sys.exit(1)
    
    # Run the MCP server
    try:
        subprocess.run([venv_python, mcp_server_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running MCP server: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("MCP server stopped", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
