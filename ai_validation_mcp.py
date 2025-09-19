#!/usr/bin/env python3
"""
AI Validation MCP Server

A Model Context Protocol server that provides world-class prompt engineering
capabilities directly integrated with Cursor IDE.

This server acts as an intelligent prompt optimizer that automatically enhances
prompts before they are sent to LLMs, ensuring maximum effectiveness.
"""

import asyncio
import json
import logging
from typing import Any, Sequence

import mcp
import mcp.types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-validation-mcp")

# Initialize the MCP server
server = Server("ai-validation-server")

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

def generate_few_shot_examples(prompt: str) -> str:
    """Generate relevant few-shot examples based on prompt content."""
    if 'code' in prompt.lower() or 'programming' in prompt.lower():
        return """Example 1: 
Q: "How do I implement a binary search?"
A: "Here's a clean Python implementation with explanation..."

Example 2:
Q: "Optimize this SQL query"
A: "I'll analyze your query and provide 3 specific optimizations..."
"""
    elif 'write' in prompt.lower() or 'content' in prompt.lower():
        return """Example 1:
Q: "Write a product description"
A: "I'll create a compelling description focusing on benefits, features, and emotional appeal..."

Example 2:
Q: "Improve this email"
A: "Here's the enhanced version with better structure and persuasive language..."
"""
    return ""

def determine_expert_role(prompt: str) -> str:
    """Determine the most appropriate expert role based on prompt content."""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ['code', 'programming', 'software', 'debug']):
        return "a senior software engineer with 10+ years of experience in multiple programming languages and best practices"
    elif any(word in prompt_lower for word in ['write', 'content', 'marketing', 'copy']):
        return "an expert copywriter and content strategist with deep understanding of persuasive writing"
    elif any(word in prompt_lower for word in ['analyze', 'data', 'research']):
        return "a data analyst and research expert skilled in systematic analysis and insight generation"
    elif any(word in prompt_lower for word in ['design', 'ui', 'ux', 'interface']):
        return "a senior UX/UI designer with expertise in user-centered design and interface optimization"
    elif any(word in prompt_lower for word in ['business', 'strategy', 'plan']):
        return "a business strategy consultant with extensive experience in strategic planning and execution"
    
    return ""

def apply_model_specific_rules(prompt: str, model: str) -> str:
    """Apply model-specific optimizations."""
    model_lower = model.lower()
    
    if 'gpt' in model_lower:
        return "Note: This prompt is optimized for GPT models. Consider using structured formatting and clear role definitions for best results."
    elif 'claude' in model_lower:
        return "Note: This prompt is optimized for Claude. Leverage its strength in detailed analysis and nuanced reasoning."
    elif 'gemini' in model_lower:
        return "Note: This prompt is optimized for Gemini. Take advantage of its multimodal capabilities and factual accuracy."
    
    return ""

def generate_recommendations(analysis: dict, original_prompt: str, rules: list) -> list:
    """Generate specific improvement recommendations."""
    recommendations = []
    
    if analysis['clarity_score'] < 0.5:
        recommendations.append("Consider adding more specific details and context to improve clarity")
    
    if not analysis['has_examples'] and analysis['needs_examples']:
        recommendations.append("Add concrete examples to illustrate your requirements")
    
    if not analysis['has_constraints'] and analysis['word_count'] > 20:
        recommendations.append("Define clear constraints or requirements for better results")
    
    if analysis['needs_structure'] and 'structured_output' not in rules:
        recommendations.append("Enable 'structured_output' rule for better organization")
    
    if analysis['needs_reasoning'] and 'chain_of_thought' not in rules:
        recommendations.append("Enable 'chain_of_thought' rule for step-by-step reasoning")
    
    return recommendations

def calculate_optimization_score(analysis: dict, rules_applied: list) -> float:
    """Calculate an optimization score based on analysis and applied rules."""
    base_score = 0.3
    
    # Scoring based on prompt structure
    if analysis['has_clear_task']:
        base_score += 0.2
    if analysis['has_context']:
        base_score += 0.1
    if analysis['has_examples']:
        base_score += 0.1
    if analysis['has_constraints']:
        base_score += 0.1
    
    # Scoring based on applied rules
    rule_bonus = min(0.2, len(rules_applied) * 0.04)
    base_score += rule_bonus
    
    return min(1.0, base_score)

def apply_engineering_rules(raw_prompt: str, rules: list = None, target_model: str = "general") -> dict:
    """
    Core prompt engineering function that applies advanced optimization techniques.
    
    Args:
        raw_prompt: The original prompt to optimize
        rules: List of rules to apply
        target_model: Target AI model for optimization
        
    Returns:
        dict: Comprehensive optimization results
    """
    if rules is None:
        rules = ['auto_optimize']
    
    # Analyze prompt structure
    analysis = analyze_prompt_structure(raw_prompt)
    
    # Start with the raw prompt
    engineered_prompt = raw_prompt
    rules_applied = []
    
    # RULE: EXPERT SYSTEM PROMPT INJECTION
    if 'expert_system' in rules or 'auto_optimize' in rules:
        expert_prompt = """You are a world-class prompt engineering expert with extensive knowledge in AI systems, language models, and optimization techniques. Your role is to help users create, analyze, and optimize prompts for maximum effectiveness across different AI models.

Your Core Identity:
- Act as a seasoned practitioner with deep understanding of LLM behavior and capabilities
- Communicate complex strategies with clarity and precision
- Approach optimization systematically and methodically
- Break down advanced techniques into actionable steps

Your communication style should be:
- Technical yet accessible, using industry terminology appropriately
- Evidence-based with references to proven techniques and methodologies
- Focused on iterative refinement and optimization
- Rich with concrete examples from various AI models and use cases

"""
        engineered_prompt = f"{expert_prompt}\n\nUser Request:\n{engineered_prompt}"
        rules_applied.append('expert_system')
    
    # RULE: CHAIN-OF-THOUGHT REASONING
    if 'chain_of_thought' in rules or (analysis.get('needs_reasoning', False) and 'auto_optimize' in rules):
        cot_instruction = "\n\nThink through this step-by-step:\n1. First, analyze the core challenge or opportunity\n2. Consider which prompt engineering methods apply and why\n3. Structure your response with clear reasoning\n4. Provide concrete, testable examples\n5. Explain the rationale behind your approach"
        engineered_prompt = f"{engineered_prompt}{cot_instruction}"
        rules_applied.append('chain_of_thought')
    
    # RULE: FEW-SHOT LEARNING ENHANCEMENT
    if 'few_shot' in rules or (analysis.get('needs_examples', False) and 'auto_optimize' in rules):
        few_shot_examples = generate_few_shot_examples(raw_prompt)
        if few_shot_examples:
            engineered_prompt = f"{engineered_prompt}\n\nHere are some examples of excellent responses:\n\n{few_shot_examples}"
            rules_applied.append('few_shot')
    
    # RULE: ROLE-PLAYING OPTIMIZATION
    if 'role_play' in rules or (analysis.get('needs_expertise', False) and 'auto_optimize' in rules):
        role_context = determine_expert_role(raw_prompt)
        if role_context:
            engineered_prompt = f"You are {role_context}.\n\n{engineered_prompt}"
            rules_applied.append('role_play')
    
    # RULE: STRUCTURED OUTPUT FORMATTING
    if 'structured_output' in rules or (analysis.get('needs_structure', False) and 'auto_optimize' in rules):
        structure_template = """

Structure your response as follows:

🔍 Quick Assessment (1-2 sentences):
Identify the core challenge or opportunity

⚡ Technique Recommendation:
Explain which prompt engineering methods apply and why

💡 Improved Prompt Example:
Provide a concrete, testable prompt the user can copy immediately

🧠 Rationale:
Explain the reasoning behind your approach and technique choices

🔄 Variations & Testing:
Suggest alternative approaches and testing strategies
"""
        engineered_prompt = f"{engineered_prompt}{structure_template}"
        rules_applied.append('structured_output')
    
    # RULE: MODEL-SPECIFIC OPTIMIZATION
    if 'model_optimize' in rules:
        model_optimization = apply_model_specific_rules(engineered_prompt, target_model)
        if model_optimization:
            engineered_prompt = f"{engineered_prompt}\n\n{model_optimization}"
            rules_applied.append('model_optimize')
    
    # RULE: CLARITY AND PRECISION ENHANCEMENT
    if 'enhance_clarity' in rules or (analysis.get('clarity_score', 0) < 0.7 and 'auto_optimize' in rules):
        clarity_instruction = "\n\nIMPORTANT: Be specific, actionable, and include concrete examples. Avoid vague language and provide step-by-step guidance where applicable."
        engineered_prompt = f"{engineered_prompt}{clarity_instruction}"
        rules_applied.append('enhance_clarity')
    
    # RULE: TESTING AND VALIDATION GUIDANCE
    if 'add_testing' in rules:
        testing_guidance = """

Testing Recommendations:
- A/B test different prompt variations
- Measure response quality against specific success metrics
- Test with different temperature settings
- Validate across multiple model runs for consistency
- Document what works best for similar use cases
"""
        engineered_prompt = f"{engineered_prompt}{testing_guidance}"
        rules_applied.append('add_testing')
    
    # Generate recommendations
    recommendations = generate_recommendations(analysis, raw_prompt, rules)
    
    # Calculate optimization score
    optimization_score = calculate_optimization_score(analysis, rules_applied)
    
    return {
        "engineered_prompt": engineered_prompt,
        "original_prompt": raw_prompt,
        "analysis": analysis,
        "rules_applied": rules_applied,
        "recommendations": recommendations,
        "optimization_score": optimization_score,
        "target_model": target_model
    }

# === MCP SERVER IMPLEMENTATION ===

@server.list_tools()
async def handle_list_tools() -> list[mcp.Tool]:
    """
    List all available prompt engineering tools.
    """
    return [
        mcp.Tool(
            name="validate_prompt",
            description="Analyze and optimize prompts using advanced prompt engineering techniques. Automatically applies expert-level optimizations.",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to analyze and optimize"
                    },
                    "rules": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Specific rules to apply: expert_system, chain_of_thought, few_shot, role_play, structured_output, model_optimize, enhance_clarity, add_testing, auto_optimize",
                        "default": ["auto_optimize"]
                    },
                    "model": {
                        "type": "string",
                        "description": "Target AI model for optimization (gpt-4, claude, gemini, etc.)",
                        "default": "general"
                    }
                },
                "required": ["prompt"]
            }
        ),
        mcp.Tool(
            name="analyze_prompt_quality",
            description="Analyze prompt structure and quality without modification. Provides detailed insights and recommendations.",
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
        ),
        mcp.Tool(
            name="get_optimization_suggestions",
            description="Get specific optimization suggestions for a prompt based on analysis.",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to get suggestions for"
                    },
                    "focus_area": {
                        "type": "string",
                        "description": "Specific area to focus on: clarity, structure, examples, reasoning, expertise",
                        "default": "all"
                    }
                },
                "required": ["prompt"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[mcp.types.TextContent]:
    """
    Handle tool calls for prompt engineering operations.
    """
    if arguments is None:
        arguments = {}
    
    if name == "validate_prompt":
        prompt = arguments.get("prompt", "")
        rules = arguments.get("rules", ["auto_optimize"])
        model = arguments.get("model", "general")
        
        if not prompt:
            return [mcp.types.TextContent(type="text", text="Error: No prompt provided")]
        
        # Apply prompt engineering
        result = apply_engineering_rules(prompt, rules, model)
        
        # Format response
        response = f"""# 🚀 AI Validation Results

## 📋 Original Prompt
```
{result['original_prompt']}
```

## ⚡ Optimized Prompt
```
{result['engineered_prompt']}
```

## 📊 Analysis Summary
- **Length**: {result['analysis']['length']} characters ({result['analysis']['word_count']} words)
- **Clarity Score**: {result['analysis']['clarity_score']:.2f}/1.0
- **Optimization Score**: {result['optimization_score']:.2f}/1.0
- **Has Clear Task**: {'✅' if result['analysis']['has_clear_task'] else '❌'}
- **Has Context**: {'✅' if result['analysis']['has_context'] else '❌'}
- **Has Examples**: {'✅' if result['analysis']['has_examples'] else '❌'}

## 🛠️ Applied Optimizations
{', '.join(result['rules_applied']) if result['rules_applied'] else 'None applied'}

## 💡 Recommendations
{chr(10).join(f"• {rec}" for rec in result['recommendations']) if result['recommendations'] else "• Prompt is well-optimized!"}

## 🎯 Target Model
Optimized for: {result['target_model']}

---
*Use the optimized prompt above for best results with your target AI model.*
"""
        
        logger.info(f"Validated prompt with {len(result['rules_applied'])} rules applied")
        return [mcp.types.TextContent(type="text", text=response)]
    
    elif name == "analyze_prompt_quality":
        prompt = arguments.get("prompt", "")
        
        if not prompt:
            return [mcp.types.TextContent(type="text", text="Error: No prompt provided")]
        
        analysis = analyze_prompt_structure(prompt)
        
        response = f"""# 🔍 Prompt Quality Analysis

## 📊 Structure Metrics
- **Length**: {analysis['length']} characters
- **Word Count**: {analysis['word_count']} words
- **Clarity Score**: {analysis['clarity_score']:.2f}/1.0
- **Question Count**: {analysis['question_count']}

## ✅ Quality Indicators
- **Clear Task**: {'✅ Yes' if analysis['has_clear_task'] else '❌ No'}
- **Sufficient Context**: {'✅ Yes' if analysis['has_context'] else '❌ No'}
- **Includes Examples**: {'✅ Yes' if analysis['has_examples'] else '❌ No'}
- **Has Constraints**: {'✅ Yes' if analysis['has_constraints'] else '❌ No'}

## 🎯 Optimization Opportunities
- **Needs Reasoning**: {'⚡ Yes' if analysis['needs_reasoning'] else '✅ No'}
- **Needs Examples**: {'⚡ Yes' if analysis['needs_examples'] else '✅ No'}
- **Needs Expertise**: {'⚡ Yes' if analysis['needs_expertise'] else '✅ No'}
- **Needs Structure**: {'⚡ Yes' if analysis['needs_structure'] else '✅ No'}

## 🎚️ Overall Assessment
{'🟢 Excellent' if analysis['clarity_score'] > 0.8 else '🟡 Good' if analysis['clarity_score'] > 0.6 else '🔴 Needs Improvement'}

---
*Use the validate_prompt tool to automatically optimize this prompt.*
"""
        
        logger.info(f"Analyzed prompt quality: {analysis['clarity_score']:.2f} clarity score")
        return [mcp.types.TextContent(type="text", text=response)]
    
    elif name == "get_optimization_suggestions":
        prompt = arguments.get("prompt", "")
        focus_area = arguments.get("focus_area", "all")
        
        if not prompt:
            return [mcp.types.TextContent(type="text", text="Error: No prompt provided")]
        
        analysis = analyze_prompt_structure(prompt)
        suggestions = []
        
        if focus_area == "all" or focus_area == "clarity":
            if analysis['clarity_score'] < 0.7:
                suggestions.append("**Clarity**: Add more specific details and concrete examples")
        
        if focus_area == "all" or focus_area == "structure":
            if analysis['needs_structure']:
                suggestions.append("**Structure**: Use bullet points or numbered lists for complex requests")
        
        if focus_area == "all" or focus_area == "examples":
            if analysis['needs_examples']:
                suggestions.append("**Examples**: Include sample inputs/outputs to clarify expectations")
        
        if focus_area == "all" or focus_area == "reasoning":
            if analysis['needs_reasoning']:
                suggestions.append("**Reasoning**: Ask for step-by-step explanations or thought processes")
        
        if focus_area == "all" or focus_area == "expertise":
            if analysis['needs_expertise']:
                role = determine_expert_role(prompt)
                if role:
                    suggestions.append(f"**Expertise**: Specify that you want response from {role}")
        
        if not suggestions:
            suggestions.append("**Great!** Your prompt is well-structured. Consider using auto_optimize for minor enhancements.")
        
        response = f"""# 💡 Optimization Suggestions

## 🎯 Focus Area: {focus_area.title()}

## 📝 Recommendations
{chr(10).join(f"{i+1}. {sug}" for i, sug in enumerate(suggestions))}

## 🛠️ Quick Fixes
- **Add constraints**: Use words like "must", "should", "requirement"
- **Improve specificity**: Replace vague terms with concrete descriptions
- **Set format**: Specify desired output format (list, table, code, etc.)
- **Define scope**: Clearly state what should and shouldn't be included

## ⚡ Auto-Optimization
Run `validate_prompt` with `auto_optimize` rule for automatic improvements.

---
*These suggestions are based on analysis of your prompt structure and content.*
"""
        
        logger.info(f"Generated {len(suggestions)} optimization suggestions")
        return [mcp.types.TextContent(type="text", text=response)]
    
    else:
        return [mcp.types.TextContent(type="text", text=f"Error: Unknown tool '{name}'")]

async def main():
    """Main entry point for the MCP server."""
    # Use stdin/stdout for communication with Cursor
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            mcp.InitializeResult(
                protocolVersion="2024-11-05",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
                serverInfo=mcp.Implementation(
                    name="ai-validation-server",
                    version="2.0.0",
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
