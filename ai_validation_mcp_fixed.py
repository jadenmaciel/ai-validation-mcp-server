#!/usr/bin/env python3
"""
AI Validation MCP Server - Fixed Implementation

A working Model Context Protocol server that provides automatic prompt optimization.
This version implements proper MCP protocol for Cursor IDE integration.
"""

import asyncio
import json
import logging
import sys
from typing import Any, Sequence

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ai-validation-mcp")

try:
    import mcp.server.stdio
    import mcp.types as types
    from mcp.server import Server
except ImportError:
    logger.error("MCP library not found. Please install with: pip install mcp")
    sys.exit(1)

# Initialize the MCP server
app = Server("ai-validation-server")

# === PROMPT ENGINEERING CORE FUNCTIONS ===

def analyze_prompt_structure(prompt: str) -> dict:
    """Analyze the structure and quality of a prompt."""
    analysis = {
        "length": len(prompt),
        "word_count": len(prompt.split()),
        "has_clear_task": bool(any(word in prompt.lower() for word in ['analyze', 'create', 'explain', 'generate', 'write', 'help'])),
        "has_context": len(prompt.split()) > 10,
        "has_examples": 'example' in prompt.lower() or 'for instance' in prompt.lower(),
        "has_constraints": any(word in prompt.lower() for word in ['must', 'should', 'requirement', 'constraint', 'limit']),
        "question_count": prompt.count('?'),
        "needs_reasoning": any(word in prompt.lower() for word in ['why', 'how', 'explain', 'analyze', 'compare']),
        "needs_examples": prompt.count('?') > 0 and len(prompt.split()) < 20,
        "needs_expertise": any(domain in prompt.lower() for domain in ['code', 'technical', 'programming', 'engineering', 'scientific', 'medical', 'legal']),
        "needs_structure": len(prompt.split()) > 30 or prompt.count('?') > 2,
        "clarity_score": min(1.0, len([word for word in prompt.split() if len(word) > 3]) / max(10, len(prompt.split())))
    }
    return analysis

def apply_expert_optimization(prompt: str) -> str:
    """Apply expert-level prompt optimization."""
    analysis = analyze_prompt_structure(prompt)
    optimized_prompt = prompt
    
    # Add expert system identity
    expert_prefix = """You are a world-class expert with deep knowledge and extensive experience. Your responses should be:
- Technically accurate and comprehensive
- Clear and well-structured
- Rich with practical examples and insights
- Evidence-based with proven methodologies

"""
    
    # Add chain-of-thought for complex queries
    if analysis['needs_reasoning']:
        reasoning_suffix = """

Think through this step-by-step:
1. Analyze the core challenge or opportunity
2. Consider multiple approaches and their trade-offs
3. Provide concrete, actionable recommendations
4. Explain your reasoning and methodology"""
        optimized_prompt += reasoning_suffix
    
    # Add structure for complex requests
    if analysis['needs_structure']:
        structure_suffix = """

Please structure your response with:
🔍 Analysis: Brief assessment of the situation
💡 Solution: Clear, actionable recommendations  
🛠️ Implementation: Step-by-step guidance
📊 Examples: Concrete examples where applicable"""
        optimized_prompt += structure_suffix
    
    # Add expertise context
    if analysis['needs_expertise']:
        if 'code' in prompt.lower() or 'programming' in prompt.lower():
            expert_context = "\n\nAs a senior software engineer with 10+ years of experience, "
        elif 'write' in prompt.lower() or 'content' in prompt.lower():
            expert_context = "\n\nAs an expert content strategist and copywriter, "
        elif 'analyze' in prompt.lower() or 'data' in prompt.lower():
            expert_context = "\n\nAs a data analyst and research expert, "
        else:
            expert_context = "\n\nAs a domain expert, "
        
        optimized_prompt = expert_context + optimized_prompt
    
    return expert_prefix + optimized_prompt

# === MCP SERVER IMPLEMENTATION ===

@app.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="optimize_prompt",
            description="Automatically optimize any prompt using expert-level prompt engineering techniques",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to optimize"
                    }
                },
                "required": ["prompt"]
            }
        ),
        types.Tool(
            name="analyze_prompt",
            description="Analyze prompt quality and structure",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to analyze"
                    }
                },
                "required": ["prompt"]
            }
        )
    ]

@app.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    """Handle tool calls."""
    if arguments is None:
        arguments = {}
    
    if name == "optimize_prompt":
        prompt = arguments.get("prompt", "")
        if not prompt:
            return [types.TextContent(type="text", text="Error: No prompt provided")]
        
        optimized = apply_expert_optimization(prompt)
        analysis = analyze_prompt_structure(prompt)
        
        response = f"""# 🚀 Optimized Prompt

## Original:
{prompt}

## Optimized:
{optimized}

## Quality Score: {analysis['clarity_score']:.2f}/1.0
Applied optimizations based on prompt analysis.
"""
        return [types.TextContent(type="text", text=response)]
    
    elif name == "analyze_prompt":
        prompt = arguments.get("prompt", "")
        if not prompt:
            return [types.TextContent(type="text", text="Error: No prompt provided")]
        
        analysis = analyze_prompt_structure(prompt)
        
        response = f"""# 📊 Prompt Analysis

**Length**: {analysis['length']} characters ({analysis['word_count']} words)
**Clarity Score**: {analysis['clarity_score']:.2f}/1.0

**Structure Assessment**:
- Clear Task: {'✅' if analysis['has_clear_task'] else '❌'}
- Sufficient Context: {'✅' if analysis['has_context'] else '❌'}
- Includes Examples: {'✅' if analysis['has_examples'] else '❌'}
- Has Constraints: {'✅' if analysis['has_constraints'] else '❌'}

**Optimization Opportunities**:
- Needs Reasoning: {'⚡' if analysis['needs_reasoning'] else '✅'}
- Needs Examples: {'⚡' if analysis['needs_examples'] else '✅'}
- Needs Expertise: {'⚡' if analysis['needs_expertise'] else '✅'}
- Needs Structure: {'⚡' if analysis['needs_structure'] else '✅'}
"""
        return [types.TextContent(type="text", text=response)]
    
    return [types.TextContent(type="text", text=f"Unknown tool: {name}")]

@app.list_prompts()
async def handle_list_prompts() -> list[types.Prompt]:
    """List available prompts for automatic optimization."""
    return [
        types.Prompt(
            name="auto_optimize",
            description="Automatically optimize any prompt with expert techniques",
            arguments=[
                types.PromptArgument(
                    name="user_prompt",
                    description="The user's original prompt to optimize",
                    required=True
                )
            ]
        )
    ]

@app.get_prompt()
async def handle_get_prompt(name: str, arguments: dict | None) -> types.GetPromptResult:
    """Handle prompt requests for automatic optimization."""
    if arguments is None:
        arguments = {}
    
    if name == "auto_optimize":
        user_prompt = arguments.get("user_prompt", "")
        if not user_prompt:
            return types.GetPromptResult(
                description="Error: No prompt provided",
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(type="text", text="Error: No prompt provided for optimization")
                    )
                ]
            )
        
        # Apply automatic optimization
        optimized_prompt = apply_expert_optimization(user_prompt)
        
        return types.GetPromptResult(
            description=f"Auto-optimized prompt with expert techniques",
            messages=[
                types.PromptMessage(
                    role="user", 
                    content=types.TextContent(type="text", text=optimized_prompt)
                )
            ]
        )
    
    return types.GetPromptResult(
        description="Unknown prompt",
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(type="text", text=f"Unknown prompt: {name}")
            )
        ]
    )

@app.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    """List available resources."""
    return [
        types.Resource(
            uri="prompt://optimization/guide",
            name="Prompt Optimization Guide",
            description="Guide for prompt optimization techniques",
            mimeType="text/plain"
        )
    ]

@app.read_resource()
async def handle_read_resource(uri: str) -> str:
    """Handle resource reads."""
    if uri == "prompt://optimization/guide":
        return """# Prompt Optimization Guide

This MCP server automatically optimizes prompts using:

1. **Expert Identity Injection**: Adds professional expertise context
2. **Chain-of-Thought**: Adds reasoning structure for complex queries  
3. **Structured Output**: Organizes responses with clear sections
4. **Domain Expertise**: Applies relevant expert personas
5. **Clarity Enhancement**: Improves specificity and actionability

Use the 'auto_optimize' prompt to automatically enhance any user input.
"""
    
    return f"Resource not found: {uri}"

async def main():
    """Main entry point for the MCP server."""
    # Use stdin/stdout for communication with Cursor
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)
