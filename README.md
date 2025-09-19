# 🚀 AI Validation MCP Server - Automatic Prompt Optimization

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **fully automatic prompt optimization** Model Context Protocol (MCP) server that enhances every prompt with world-class prompt engineering techniques. No manual intervention required - just install, configure, and every prompt gets automatically optimized!

## ✨ What It Does

🎯 **Fully Automatic**: Every prompt you send gets automatically enhanced with expert techniques  
🧠 **Expert-Level Optimization**: Applies world-class prompt engineering without any manual work  
🔍 **Visual Feedback**: Shows exactly what optimizations were applied to each prompt  
⚡ **Smart Detection**: Automatically detects technical, creative, or analytical content  
🎨 **Domain Expertise**: Adds appropriate expert context based on your prompt content  

## 🎯 Example: Before vs After

### **Your Original Prompt:**
```
How do I write better Python code?
```

### **What You'll See (Automatically Enhanced):**
```
🚀 **AI VALIDATION: PROMPT AUTOMATICALLY OPTIMIZED** 🚀

🔧 **ORIGINAL PROMPT**: How do I write better Python code?

✨ **AUTO-OPTIMIZED VERSION**: Please provide a comprehensive and detailed response with specific examples and practical guidance.

As a senior technical expert, please include best practices, potential pitfalls, and real-world implementation considerations.

Please explain your reasoning and methodology.

🔍 **OPTIMIZATIONS APPLIED**:
  • 🎯 Enhanced clarity and detail requirements
  • 🛠️ Technical expertise context added  
  • 🧠 Reasoning and methodology requested
  • 🌟 Expert system identity applied

---

[Then you get a comprehensive expert response with examples, best practices, step-by-step guidance, etc.]
```

## 🚀 Quick Start

### **Step 1: Install**

```bash
# Clone the repository
git clone https://github.com/jadenmaciel/ai-validation-mcp-server.git
cd ai-validation-mcp-server

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### **Step 2: Configure Cursor**

Add this to your `~/.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "ai_validation_auto": {
      "command": "python3",
      "args": ["/path/to/ai-validation-mcp-server/run_mcp_auto.py"]
    }
  }
}
```

**Important**: Replace `/path/to/ai-validation-mcp-server/` with your actual path!

### **Step 3: Restart Cursor**

1. **Close all Cursor windows**
2. **Quit Cursor entirely** (Cmd+Q / Ctrl+Q)
3. **Restart Cursor**

### **Step 4: Verify It's Working**

1. Go to **Settings** → **Features** → **MCP Servers**
2. Look for `ai_validation_auto` with a **green dot** ✅
3. Try asking any question - you should see the optimization indicators!

## 🎯 Automatic Optimizations Applied

The server automatically detects your prompt type and applies appropriate enhancements:

### **🛠️ Technical Prompts** (code, programming, technical questions)
- Adds senior technical expert context
- Requests best practices and pitfalls
- Asks for implementation considerations

### **🎨 Creative Prompts** (writing, design, creative tasks)
- Adds creative professional context
- Requests innovative approaches and options
- Asks for creative insights

### **📊 Analytical Prompts** (data, research, analysis)
- Adds analytical expert context
- Requests systematic analysis
- Asks for data-driven insights

### **🎯 All Prompts Get:**
- Enhanced clarity and detail requirements
- Structured response formatting (when appropriate)
- Concrete examples and illustrations
- Step-by-step explanations for complex topics
- Expert-level system identity

## 📁 Project Structure

```
ai-validation-mcp-server/
├── ai_validation_mcp_auto.py    # 🚀 Main automatic optimization server
├── run_mcp_auto.py              # 🔧 Server runner with venv handling
├── requirements.txt             # 📦 Python dependencies
├── README.md                    # 📖 This documentation
├── LICENSE                      # ⚖️ MIT License
├── .gitignore                   # 🙈 Git ignore rules
└── venv/                        # 🐍 Virtual environment (auto-created)
```

## 🔧 Configuration Options

The server works automatically with zero configuration, but you can customize by editing `ai_validation_mcp_auto.py`:

- **Modify optimization rules** in `optimize_user_prompt()`
- **Adjust expert system prompt** in `create_expert_system_prompt()`
- **Change detection patterns** for different prompt types

## 🔍 Troubleshooting

### **Green dot not showing?**
```bash
# Test the server manually
cd /path/to/ai-validation-mcp-server
source venv/bin/activate
python ai_validation_mcp_auto.py
# Should show: "🚀 Starting AI Validation MCP Server (Automatic Mode)"
```

### **No optimization indicators?**
1. Verify the green dot is present in MCP settings
2. Check absolute path in mcp.json is correct
3. Ensure Cursor was completely restarted (not just closed)

### **Permissions issues?**
```bash
chmod +x /path/to/ai-validation-mcp-server/run_mcp_auto.py
chmod +x /path/to/ai-validation-mcp-server/ai_validation_mcp_auto.py
```

### **Check logs:**
- In Cursor: `Ctrl+Shift+U` → "MCP Logs"
- Look for "🚀 Starting AI Validation MCP Server (Automatic Mode)"

## 🎉 What You Get

✅ **Zero Manual Work** - Every prompt automatically optimized  
✅ **Expert-Level Responses** - World-class prompt engineering applied  
✅ **Visual Confirmation** - See exactly what optimizations were applied  
✅ **Smart Detection** - Appropriate expertise based on content  
✅ **Better Results** - More comprehensive, structured, actionable responses  

## 🤝 Contributing

Contributions welcome! Feel free to:
- Improve optimization techniques
- Add new prompt detection patterns  
- Enhance the expert system prompts
- Submit bug reports or feature requests

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Transform every prompt into an expertly optimized query automatically!** 🚀

**Repository**: https://github.com/jadenmaciel/ai-validation-mcp-server