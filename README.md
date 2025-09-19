# 🚀 AI Validation MCP Server

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **world-class prompt engineering** Model Context Protocol (MCP) server that automatically optimizes prompts before they're sent to LLMs. This server acts as an intelligent middleware that applies advanced prompt engineering techniques, ensuring maximum effectiveness across different AI models.

## ✨ Features

- 🧠 **Expert-Level Optimization**: World-class prompt engineering techniques
- ⚡ **Automatic Enhancement**: Smart analysis and optimization based on prompt content
- 🎯 **Model-Specific**: Tailored optimizations for GPT, Claude, Gemini, and more
- 🔍 **Intelligent Analysis**: Comprehensive prompt quality assessment
- 🛠️ **Multiple Tools**: Validation, analysis, and suggestion generation
- 🚀 **Cursor Integration**: Native MCP integration with Cursor IDE
- 📊 **Quality Scoring**: Optimization and clarity metrics

## 🎯 Use Cases

- **Before LLM Requests**: Automatically enhance prompts for better results
- **Prompt Analysis**: Understand prompt quality and optimization opportunities
- **A/B Testing**: Generate variations for prompt optimization testing
- **Education**: Learn prompt engineering best practices
- **Quality Assurance**: Ensure prompts meet professional standards

## 🛠️ Available Tools

### 1. `validate_prompt`
**Purpose**: Automatically optimize prompts using advanced prompt engineering techniques

**Parameters**:
- `prompt` (required) - The prompt to optimize
- `rules` (optional) - Specific optimization rules to apply
- `model` (optional) - Target AI model (gpt-4, claude, gemini, etc.)

**Rules Available**:
- `expert_system` - Inject world-class expertise and identity
- `chain_of_thought` - Add step-by-step reasoning instructions
- `few_shot` - Include relevant examples based on content
- `role_play` - Assign appropriate expert persona
- `structured_output` - Format with clear sections and structure
- `model_optimize` - Apply model-specific optimizations
- `enhance_clarity` - Improve specificity and actionability
- `add_testing` - Include A/B testing and validation guidance
- `auto_optimize` - Automatically apply optimal rules (default)

### 2. `analyze_prompt_quality`
**Purpose**: Analyze prompt structure and quality without modification

**Parameters**:
- `prompt` (required) - The prompt to analyze

**Returns**: Detailed quality metrics, structure analysis, and optimization opportunities

### 3. `get_optimization_suggestions`
**Purpose**: Get specific improvement recommendations

**Parameters**:
- `prompt` (required) - The prompt to analyze
- `focus_area` (optional) - Specific area to focus on (clarity, structure, examples, reasoning, expertise)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Cursor IDE (for MCP integration)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jadenmaciel/ai-validation-mcp-server.git
   cd ai-validation-mcp-server
   ```

2. **Set up virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Test the server**:
   ```bash
   python ai_validation_mcp.py
   ```

### Cursor IDE Integration

1. **Update your `mcp.json`** (usually at `~/.cursor/mcp.json`):
   ```json
   {
     "mcpServers": {
       "ai-validation": {
         "command": "python3",
         "args": ["/path/to/ai-validation-mcp-server/run_mcp_server.py"]
       }
     }
   }
   ```

2. **Restart Cursor IDE** completely

3. **Verify integration**: The AI Validation tools should now be available in Cursor

## 📖 Usage Examples

### Basic Prompt Optimization
```
Tool: validate_prompt
Input: {
  "prompt": "How do I write code?",
  "rules": ["auto_optimize"],
  "model": "gpt-4"
}
```

**Result**: A dramatically enhanced prompt with expert identity, structured output, and model-specific optimizations.

### Quality Analysis
```
Tool: analyze_prompt_quality
Input: {
  "prompt": "Explain machine learning to me"
}
```

**Result**: Detailed analysis including clarity score, structure metrics, and optimization opportunities.

### Get Suggestions
```
Tool: get_optimization_suggestions
Input: {
  "prompt": "Write a function",
  "focus_area": "clarity"
}
```

**Result**: Specific recommendations for improving prompt clarity and effectiveness.

## 🧠 Prompt Engineering Techniques

This server implements advanced techniques including:

- **Expert System Prompting**: Injecting world-class expertise and identity
- **Chain-of-Thought Reasoning**: Step-by-step analytical approaches
- **Few-Shot Learning**: Relevant examples based on prompt content
- **Role-Playing**: Appropriate expert persona assignment
- **Structured Output**: Clear formatting with sections and organization
- **Model-Specific Optimization**: Tailored for different AI models
- **Clarity Enhancement**: Improved specificity and actionability
- **Testing Guidance**: A/B testing and validation recommendations

## 📊 Quality Metrics

The server provides comprehensive quality scoring:

- **Clarity Score**: Measures prompt specificity and actionability (0.0-1.0)
- **Optimization Score**: Overall prompt effectiveness after optimization (0.0-1.0)
- **Structure Analysis**: Task clarity, context, examples, constraints detection
- **Model Compatibility**: Suitability assessment for target AI models

## 🔧 Configuration

### Environment Variables

Create a `.env` file for custom configuration:

```env
# Logging level
LOG_LEVEL=INFO

# Default optimization rules
DEFAULT_RULES=auto_optimize

# Default target model
DEFAULT_MODEL=general
```

### Custom Rules

You can extend the server with custom optimization rules by modifying the `apply_engineering_rules()` function in `ai_validation_mcp.py`.

## 📁 Project Structure

```
ai-validation-mcp-server/
├── ai_validation_mcp.py          # Main MCP server implementation
├── run_mcp_server.py              # Server runner with venv handling
├── mcp_server.py                  # Legacy HTTP server (optional)
├── requirements.txt               # Python dependencies
├── MCP_INTEGRATION_GUIDE.md       # Detailed integration guide
├── README.md                      # This file
├── .gitignore                     # Git ignore rules
├── venv/                          # Virtual environment (auto-created)
└── examples/                      # Usage examples (coming soon)
```

## 🔍 Troubleshooting

### Common Issues

**Server not starting**:
```bash
# Check virtual environment
ls -la venv/bin/python

# Test manually
source venv/bin/activate
python ai_validation_mcp.py
```

**Tools not appearing in Cursor**:
1. Verify `mcp.json` syntax
2. Ensure absolute paths are used
3. Restart Cursor completely
4. Check Cursor's MCP server logs

**Permission issues**:
```bash
chmod +x run_mcp_server.py
chmod +x ai_validation_mcp.py
```

### Debug Mode

Run with debug logging:
```bash
LOG_LEVEL=DEBUG python ai_validation_mcp.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on the [Model Context Protocol](https://modelcontextprotocol.io/) standard
- Inspired by prompt engineering best practices from the AI community
- Designed for seamless integration with [Cursor IDE](https://cursor.sh/)

## 📞 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#-troubleshooting)
2. Review the [MCP Integration Guide](MCP_INTEGRATION_GUIDE.md)
3. Open an issue on GitHub
4. Check existing issues for similar problems

---

**Transform your prompts from good to extraordinary with AI Validation MCP Server!** 🚀
