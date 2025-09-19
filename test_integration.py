#!/usr/bin/env python3
"""
Example script showing how to integrate the AI Validation Server
with your existing workflow.
"""

import requests
import json

def validate_and_optimize_prompt(prompt, rules=None):
    """
    Send a prompt to the AI Validation Server for optimization.
    
    Args:
        prompt (str): The raw prompt to optimize
        rules (list): List of rules to apply
        
    Returns:
        dict: The validation response with optimized prompt
    """
    if rules is None:
        rules = ["expert_system", "chain_of_thought", "structured_output"]
    
    payload = {
        "request_id": "integration-test",
        "raw_prompt": prompt,
        "config": {
            "model": "gpt-4",
            "apply_rules": rules
        }
    }
    
    try:
        response = requests.post(
            "http://localhost:5001/validate-prompt",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ AI Validation Server not running. Start it with: ./start_server.sh")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    """Test the integration."""
    print("🧪 Testing AI Validation Server Integration")
    print("=" * 50)
    
    # Test prompt
    raw_prompt = "How do I write a fast sort algorithm?"
    
    print(f"📝 Original prompt: {raw_prompt}")
    print("\n🔄 Sending to validation server...")
    
    result = validate_and_optimize_prompt(raw_prompt)
    
    if result:
        print("\n✅ Validation successful!")
        print(f"🎯 Optimization score: {result.get('optimization_score', 'N/A')}")
        print(f"🛠️ Rules applied: {', '.join(result.get('rules_applied', []))}")
        print(f"💡 Recommendations: {len(result.get('recommendations', []))} items")
        
        print("\n📋 Optimized prompt:")
        print("-" * 30)
        print(result['engineered_prompt'][:500] + "..." if len(result['engineered_prompt']) > 500 else result['engineered_prompt'])
        
        # Now you would send this optimized prompt to your actual LLM
        print("\n🚀 Ready to send optimized prompt to LLM!")
        
    else:
        print("\n❌ Validation failed!")

if __name__ == "__main__":
    main()
