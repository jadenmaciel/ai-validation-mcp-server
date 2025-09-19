# 🎯 Cursor IDE Setup Guide - AI Validation MCP Server

## 🚨 **Current Issue Resolution**

Your MCP server wasn't working because of several issues that have now been fixed:

1. ❌ **Incorrect MCP Protocol Implementation** → ✅ **Fixed with proper MCP SDK usage**
2. ❌ **Missing Prompts for Auto-Optimization** → ✅ **Added `auto_optimize` prompt**
3. ❌ **Configuration Issues** → ✅ **Updated mcp.json with correct paths**
4. ❌ **Server Name with Hyphens** → ✅ **Changed to `ai_validation` (underscores)**

## 🔧 **Fixed Implementation**

### **New Files Created:**
- `ai_validation_mcp_fixed.py` - Working MCP server with proper protocol
- `run_mcp_fixed.py` - Fixed runner script
- `mcp_config.json` - Correct configuration template

## 📋 **Step-by-Step Setup**

### **Step 1: Update Your mcp.json**

**Location**: `~/.cursor/mcp.json` (or create if it doesn't exist)

**Replace your current mcp.json with this:**

```json
{
  "mcpServers": {
    "ai_validation": {
      "command": "python3",
      "args": ["/home/jaden/ai-validation-server/run_mcp_fixed.py"]
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

### **Step 2: Restart Cursor Completely**

1. **Close all Cursor windows**
2. **Quit Cursor entirely** (not just close windows)
3. **Restart Cursor**

### **Step 3: Verify MCP Server Status**

1. Open Cursor
2. Go to **Settings** → **Features** → **MCP Servers**
3. Look for `ai_validation` with a **green dot** ✅
4. If you see a red dot ❌, check the logs

### **Step 4: Check Available Tools**

In Cursor chat, you should now see these tools available:
- 🛠️ **optimize_prompt** - Automatically optimize prompts
- 📊 **analyze_prompt** - Analyze prompt quality
- ⚡ **auto_optimize** (prompt) - For automatic optimization

## 🚀 **Automatic Prompt Optimization**

### **Method 1: Using the Auto-Optimize Prompt**

Instead of typing your prompt directly, use:

```
@auto_optimize user_prompt="Your original prompt here"
```

This will automatically optimize your prompt before sending it to the LLM.

### **Method 2: Manual Tool Usage**

Use the `optimize_prompt` tool:

```
Use optimize_prompt tool with:
prompt: "Your prompt to optimize"
```

## 🔍 **Troubleshooting**

### **Issue: Server Shows Red Dot**

**Solution:**
```bash
cd /home/jaden/ai-validation-server
source venv/bin/activate
python ai_validation_mcp_fixed.py
# Check for any error messages
```

### **Issue: Tools Not Appearing**

**Fixes:**
1. **Check mcp.json syntax** - Use a JSON validator
2. **Verify absolute paths** - Ensure `/home/jaden/ai-validation-server/run_mcp_fixed.py` exists
3. **Restart Cursor completely** - Full quit and restart
4. **Check permissions**:
   ```bash
   chmod +x /home/jaden/ai-validation-server/run_mcp_fixed.py
   chmod +x /home/jaden/ai-validation-server/ai_validation_mcp_fixed.py
   ```

### **Issue: Path Problems**

If you moved the directory, update the path in mcp.json:
```json
"args": ["/your/new/path/ai-validation-server/run_mcp_fixed.py"]
```

### **Issue: Virtual Environment**

Recreate if needed:
```bash
cd /home/jaden/ai-validation-server
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install mcp
```

## 📊 **Verification Steps**

### **1. Test MCP Server Manually**
```bash
cd /home/jaden/ai-validation-server
source venv/bin/activate
timeout 5 python ai_validation_mcp_fixed.py
# Should exit cleanly without errors
```

### **2. Check Cursor Logs**
1. Open Cursor
2. Press `Ctrl+Shift+U` (Output panel)
3. Select "MCP Logs" from dropdown
4. Look for `ai_validation` server messages

### **3. Test Tools in Cursor**
Try using:
```
@optimize_prompt prompt="How do I write better code?"
```

## 🎯 **Expected Behavior**

Once working correctly:

1. **Tools Available**: You'll see `optimize_prompt` and `analyze_prompt` in tool suggestions
2. **Prompts Available**: You'll see `auto_optimize` in prompt suggestions  
3. **Automatic Optimization**: Using `@auto_optimize` will enhance prompts before sending to LLMs
4. **Green Status**: MCP server shows green dot in settings

## 💡 **Usage Examples**

### **Automatic Optimization:**
```
@auto_optimize user_prompt="Explain machine learning"
```

**Result**: Automatically optimized with expert identity, structure, and enhanced clarity

### **Manual Tool Usage:**
```
Use the optimize_prompt tool with this prompt: "Write a Python function"
```

**Result**: Returns optimized version with expert techniques applied

## 🚨 **Important Notes**

1. **Use underscores** in server names (not hyphens)
2. **Absolute paths** in mcp.json configuration
3. **Complete restart** of Cursor required after changes
4. **Check logs** if tools don't appear
5. **Virtual environment** must be properly set up

---

**Your AI Validation MCP Server should now work correctly with automatic prompt optimization!** 🚀
