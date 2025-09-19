# AI Validation MCP Server Integration Guide

## 🚀 Overview

Your AI Validation server has been converted to a true Model Context Protocol (MCP) server that integrates directly with Cursor IDE. This allows automatic prompt engineering on every request!

## 📁 Files Created

- `ai_validation_mcp.py` - The main MCP server implementation
- `run_mcp_server.py` - Runner script that handles virtual environment
- `venv/` - Python virtual environment with MCP dependencies

## 🔧 Integration Steps

### Step 1: Update Your mcp.json

Add this to your `mcp.json` file:

```json
{
  "mcpServers": {
    "ai-validation": {
      "command": "python3",
      "args": ["/home/jaden/ai-validation-server/run_mcp_server.py"]
    },
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "mcp-chromedevtools"]
    },
    "database-inspector": {
      "command": "npx",
      "args": ["-y", "@executeautomation/mcp-database-server"]
    }
  }
}
```

### Step 2: Restart Cursor IDE

After updating mcp.json, restart Cursor IDE completely to load the new server.

### Step 3: Verify Integration

You should see the AI Validation server available in Cursor with these tools:
- `validate_prompt` - Optimize prompts automatically
- `analyze_prompt_quality` - Analyze prompt structure
- `get_optimization_suggestions` - Get specific improvement suggestions

## 🛠️ Available Tools

### 1. validate_prompt
**Purpose**: Automatically optimize prompts using world-class prompt engineering techniques

**Parameters**:
- `prompt` (required) - The prompt to optimize
- `rules` (optional) - Specific rules to apply: 
  - `expert_system` - Inject expert identity and knowledge
  - `chain_of_thought` - Add step-by-step reasoning
  - `few_shot` - Include relevant examples
  - `role_play` - Assign expert persona
  - `structured_output` - Format with clear sections
  - `model_optimize` - Apply model-specific optimizations
  - `enhance_clarity` - Improve specificity and actionability
  - `add_testing` - Include A/B testing guidance
  - `auto_optimize` - Automatically apply optimal rules (default)
- `model` (optional) - Target model (gpt-4, claude, gemini, etc.)

### 2. analyze_prompt_quality
**Purpose**: Analyze prompt structure without modification

**Parameters**:
- `prompt` (required) - The prompt to analyze

### 3. get_optimization_suggestions
**Purpose**: Get specific suggestions for improvement

**Parameters**:
- `prompt` (required) - The prompt to analyze
- `focus_area` (optional) - Specific area: clarity, structure, examples, reasoning, expertise

## 🎯 Usage in Cursor

Once integrated, you can:

1. **Manual Optimization**: Use the tools directly in Cursor to optimize prompts before sending to LLMs
2. **Analysis**: Analyze existing prompts to understand quality and optimization opportunities
3. **Suggestions**: Get specific recommendations for prompt improvements

## 🔍 Example Usage

### Optimize a Prompt
```
Tool: validate_prompt
Prompt: "How do I write code?"
Rules: ["auto_optimize"]
Model: "gpt-4"
```

### Analyze Quality
```
Tool: analyze_prompt_quality
Prompt: "Explain machine learning to me"
```

### Get Suggestions
```
Tool: get_optimization_suggestions
Prompt: "Write a function"
Focus Area: "clarity"
```

## 🐛 Troubleshooting

### Server Not Starting
1. Check virtual environment: `ls -la /home/jaden/ai-validation-server/venv/`
2. Test manually: `python3 /home/jaden/ai-validation-server/run_mcp_server.py`
3. Check dependencies: `source venv/bin/activate && pip list | grep mcp`

### Tools Not Appearing
1. Verify mcp.json syntax is correct
2. Ensure Cursor was completely restarted
3. Check Cursor's MCP server logs

### Permission Issues
```bash
chmod +x /home/jaden/ai-validation-server/run_mcp_server.py
chmod +x /home/jaden/ai-validation-server/ai_validation_mcp.py
```

## 🚀 Benefits

✅ **Automatic Integration**: Available in every Cursor session  
✅ **World-Class Optimization**: Expert-level prompt engineering  
✅ **Intelligent Analysis**: Automatic detection of optimization needs  
✅ **Model-Specific**: Optimizations tailored to target AI models  
✅ **Real-Time**: Instant optimization without external calls  

Your prompts will now be automatically enhanced with professional prompt engineering techniques!
