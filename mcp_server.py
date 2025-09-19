#!/usr/bin/env python3
"""
AI Validation MCP (Model-Controlling Proxy) Server

A local Flask server that applies prompt engineering rules to incoming requests
before they are sent to actual LLM endpoints. This allows for rapid testing
and validation of prompt structures.

Usage:
    python mcp_server.py

The server will run on localhost:5001 and accept POST requests at /validate-prompt
"""

from flask import Flask, request, jsonify
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

def apply_engineering_rules(request_data):
    """
    Core prompt engineering function that acts as a world-class expert system.
    
    This function applies advanced prompt engineering techniques including:
    - Systematic prompt analysis and optimization
    - Advanced techniques (chain-of-thought, few-shot learning, role-playing)
    - Structure validation and improvement recommendations
    - Model-specific optimizations
    
    Args:
        request_data (dict): The incoming JSON request containing raw_prompt and config
        
    Returns:
        dict: Processed response with engineered prompt, analysis, and recommendations
    """
    # Extract data from request
    request_id = request_data.get('request_id', 'unknown')
    raw_prompt = request_data.get('raw_prompt', '')
    config = request_data.get('config', {})
    apply_rules = config.get('apply_rules', [])
    target_model = config.get('model', 'general')
    
    # Initialize response structure
    engineered_prompt = raw_prompt
    rules_applied = []
    analysis = {}
    recommendations = []
    
    # CORE PROMPT ANALYSIS
    analysis = analyze_prompt_structure(raw_prompt)
    
    # RULE: EXPERT SYSTEM PROMPT INJECTION
    if 'expert_system' in apply_rules or 'auto_optimize' in apply_rules:
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
        logger.info(f"Applied 'expert_system' rule for request {request_id}")
    
    # RULE: CHAIN-OF-THOUGHT REASONING
    if 'chain_of_thought' in apply_rules or analysis.get('needs_reasoning', False):
        cot_instruction = "\n\nThink through this step-by-step:\n1. First, analyze the core challenge or opportunity\n2. Consider which prompt engineering methods apply and why\n3. Structure your response with clear reasoning\n4. Provide concrete, testable examples\n5. Explain the rationale behind your approach"
        engineered_prompt = f"{engineered_prompt}{cot_instruction}"
        rules_applied.append('chain_of_thought')
        logger.info(f"Applied 'chain_of_thought' rule for request {request_id}")
    
    # RULE: FEW-SHOT LEARNING ENHANCEMENT
    if 'few_shot' in apply_rules or analysis.get('needs_examples', False):
        few_shot_examples = generate_few_shot_examples(raw_prompt)
        if few_shot_examples:
            engineered_prompt = f"{engineered_prompt}\n\nHere are some examples of excellent responses:\n\n{few_shot_examples}"
            rules_applied.append('few_shot')
            logger.info(f"Applied 'few_shot' rule for request {request_id}")
    
    # RULE: ROLE-PLAYING OPTIMIZATION
    if 'role_play' in apply_rules or analysis.get('needs_expertise', False):
        role_context = determine_expert_role(raw_prompt)
        if role_context:
            engineered_prompt = f"You are {role_context}.\n\n{engineered_prompt}"
            rules_applied.append('role_play')
            logger.info(f"Applied 'role_play' rule for request {request_id}")
    
    # RULE: STRUCTURED OUTPUT FORMATTING
    if 'structured_output' in apply_rules or analysis.get('needs_structure', False):
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
        logger.info(f"Applied 'structured_output' rule for request {request_id}")
    
    # RULE: MODEL-SPECIFIC OPTIMIZATION
    if 'model_optimize' in apply_rules:
        model_optimization = apply_model_specific_rules(engineered_prompt, target_model)
        if model_optimization:
            engineered_prompt = f"{engineered_prompt}\n\n{model_optimization}"
            rules_applied.append('model_optimize')
            logger.info(f"Applied 'model_optimize' rule for {target_model} for request {request_id}")
    
    # RULE: CLARITY AND PRECISION ENHANCEMENT
    if 'enhance_clarity' in apply_rules or analysis.get('clarity_score', 0) < 0.7:
        clarity_instruction = "\n\nIMPORTANT: Be specific, actionable, and include concrete examples. Avoid vague language and provide step-by-step guidance where applicable."
        engineered_prompt = f"{engineered_prompt}{clarity_instruction}"
        rules_applied.append('enhance_clarity')
        logger.info(f"Applied 'enhance_clarity' rule for request {request_id}")
    
    # RULE: TESTING AND VALIDATION GUIDANCE
    if 'add_testing' in apply_rules:
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
        logger.info(f"Applied 'add_testing' rule for request {request_id}")
    
    # GENERATE IMPROVEMENT RECOMMENDATIONS
    recommendations = generate_recommendations(analysis, raw_prompt, config)
    
    # Log analysis results
    logger.info(f"REQUEST ID: {request_id}")
    logger.info(f"PROMPT ANALYSIS: {analysis}")
    logger.info(f"RULES APPLIED: {rules_applied}")
    logger.info(f"RECOMMENDATIONS: {recommendations}")
    
    # Prepare comprehensive response
    response = {
        "request_id": request_id,
        "engineered_prompt": engineered_prompt,
        "original_prompt": raw_prompt,
        "status": "validation_success",
        "rules_applied": rules_applied,
        "prompt_analysis": analysis,
        "recommendations": recommendations,
        "optimization_score": calculate_optimization_score(analysis, rules_applied),
        "model_compatibility": assess_model_compatibility(engineered_prompt, target_model)
    }
    
    return response


def analyze_prompt_structure(prompt):
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


def generate_few_shot_examples(prompt):
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
    return None


def determine_expert_role(prompt):
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
    
    return None


def apply_model_specific_rules(prompt, model):
    """Apply model-specific optimizations."""
    model_lower = model.lower()
    
    if 'gpt' in model_lower:
        return "Note: This prompt is optimized for GPT models. Consider using structured formatting and clear role definitions for best results."
    elif 'claude' in model_lower:
        return "Note: This prompt is optimized for Claude. Leverage its strength in detailed analysis and nuanced reasoning."
    elif 'gemini' in model_lower:
        return "Note: This prompt is optimized for Gemini. Take advantage of its multimodal capabilities and factual accuracy."
    
    return None


def generate_recommendations(analysis, original_prompt, config):
    """Generate specific improvement recommendations."""
    recommendations = []
    
    if analysis['clarity_score'] < 0.5:
        recommendations.append("Consider adding more specific details and context to improve clarity")
    
    if not analysis['has_examples'] and analysis['needs_examples']:
        recommendations.append("Add concrete examples to illustrate your requirements")
    
    if not analysis['has_constraints'] and analysis['word_count'] > 20:
        recommendations.append("Define clear constraints or requirements for better results")
    
    if analysis['needs_structure'] and 'structured_output' not in config.get('apply_rules', []):
        recommendations.append("Enable 'structured_output' rule for better organization")
    
    if analysis['needs_reasoning'] and 'chain_of_thought' not in config.get('apply_rules', []):
        recommendations.append("Enable 'chain_of_thought' rule for step-by-step reasoning")
    
    return recommendations


def calculate_optimization_score(analysis, rules_applied):
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


def assess_model_compatibility(prompt, model):
    """Assess how well the prompt is suited for the target model."""
    compatibility = {
        "score": 0.8,  # Default good compatibility
        "notes": [],
        "optimizations": []
    }
    
    model_lower = model.lower()
    prompt_length = len(prompt)
    
    if 'gpt' in model_lower:
        if prompt_length > 8000:
            compatibility["notes"].append("Long prompt - consider breaking into smaller chunks")
            compatibility["score"] -= 0.1
        compatibility["optimizations"].append("Well-suited for creative and analytical tasks")
    
    elif 'claude' in model_lower:
        if prompt_length > 10000:
            compatibility["notes"].append("Very long prompt - Claude handles this well")
        compatibility["optimizations"].append("Excellent for detailed analysis and reasoning")
    
    return compatibility

@app.route('/validate-prompt', methods=['POST'])
def validate_prompt():
    """
    Main endpoint for prompt validation and engineering.
    
    Accepts JSON payload with raw prompt and configuration,
    applies engineering rules, and returns modified prompt.
    """
    try:
        # Validate content type
        if not request.is_json:
            return jsonify({
                "error": "Content-Type must be application/json",
                "status": "validation_failed"
            }), 400
        
        # Parse JSON data
        request_data = request.get_json()
        
        # Validate required fields
        if not request_data:
            return jsonify({
                "error": "Invalid JSON payload",
                "status": "validation_failed"
            }), 400
            
        if 'raw_prompt' not in request_data:
            return jsonify({
                "error": "Missing required field: raw_prompt",
                "status": "validation_failed"
            }), 400
        
        # Apply engineering rules
        response = apply_engineering_rules(request_data)
        
        # Log successful processing
        logger.info(f"Successfully processed request {response['request_id']}")
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            "error": f"Server error: {str(e)}",
            "status": "validation_failed"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint to verify server is running.
    """
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "AI Validation MCP Server"
    }), 200

@app.route('/', methods=['GET'])
def root():
    """
    Root endpoint with basic server information.
    """
    return jsonify({
        "service": "AI Validation MCP Server",
        "version": "1.0.0",
        "endpoints": {
            "validate_prompt": "POST /validate-prompt",
            "health": "GET /health"
        },
        "description": "Local server for validating and engineering AI prompts"
    }), 200

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Starting AI Validation MCP Server")
    print("=" * 60)
    print(f"Server running on: http://localhost:5001")
    print(f"Main endpoint: http://localhost:5001/validate-prompt")
    print(f"Health check: http://localhost:5001/health")
    print("=" * 60)
    print("\nExample curl command to test:")
    print("""
curl -X POST http://localhost:5001/validate-prompt \\
-H "Content-Type: application/json" \\
-d '{
  "request_id": "test-123",
  "raw_prompt": "How do I write a fast sort algorithm?",
  "config": {
    "model": "gpt-4",
    "temperature": 0.5,
    "apply_rules": ["expert_system", "chain_of_thought", "structured_output", "role_play", "model_optimize"]
  }
}'

Available rules:
- expert_system: Injects world-class prompt engineering expertise
- chain_of_thought: Adds step-by-step reasoning instructions
- few_shot: Provides relevant examples based on prompt content
- role_play: Assigns appropriate expert persona
- structured_output: Formats response with clear sections
- model_optimize: Applies model-specific optimizations
- enhance_clarity: Improves specificity and actionability
- add_testing: Includes A/B testing and validation guidance
- auto_optimize: Automatically applies optimal rules based on analysis
    """)
    print("=" * 60)
    
    # Run the Flask development server
    app.run(
        host='localhost',
        port=5001,
        debug=True,
        use_reloader=True
    )