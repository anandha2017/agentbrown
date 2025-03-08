#!/usr/bin/env python3
"""
Example script for the Banking Content Compliance Review System
This script demonstrates the system with a predefined example.
"""

import os
import json
import dotenv
from autogen import UserProxyAgent

# Import our custom modules
from agents.compliance_reviewer import create_compliance_reviewer_agent
from utils.word_count import validate_word_count
from utils.compliance_rules import check_common_issues

# Load environment variables from env.local
dotenv.load_dotenv('env.local')

# Get the OpenAI API key
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key or openai_api_key == "your_openai_api_key_here":
    raise ValueError("Please set your OpenAI API key in env.local")

# Configure OpenAI
config_list = [
    {
        "model": "gpt-4o-mini",
        "api_key": openai_api_key
    }
]

# Save config to a temporary file that autogen can read
with open("openai_config.json", "w") as f:
    json.dump(config_list, f)

# Create our compliance agent
compliance_agent = create_compliance_reviewer_agent(config_list)

# Create a user proxy that can interact with the compliance agent
user_proxy = UserProxyAgent(
    name="ExampleUser",
    human_input_mode="NEVER",  # No human input for this example
    code_execution_config={"last_n_messages": 3, "work_dir": ".", "use_docker": False},
    system_message="You are demonstrating the Banking Content Compliance Review System."
)

def run_example():
    print("Banking Content Compliance Review System - Example")
    print("------------------------------------------------")
    
    # Example content
    example_content = """Grow your money faster with our Premium Saver account. With market-leading rates and 
    instant access to your funds, there's no better place for your savings. Open an account 
    today with just £100 and watch your money grow!"""
    
    # Example word count requirements
    desktop_limit = 50
    mobile_limit = 30
    
    print(f"\nExample Content:\n\"{example_content}\"\n")
    print(f"Desktop word limit: {desktop_limit}")
    print(f"Mobile word limit: {mobile_limit}")
    
    # Validate word count
    desktop_valid, mobile_valid, word_count = validate_word_count(example_content, desktop_limit, mobile_limit)
    
    # Check for common compliance issues
    potential_issues = check_common_issues(example_content)
    issues_text = ""
    if potential_issues:
        issues_text = "\n\nPotential compliance issues detected:\n"
        for issue in potential_issues:
            issues_text += f"- {issue['description']} (found: '{issue['found']}')\n"
    
    print(f"\nAnalysis Results:")
    print(f"Word count: {word_count} words")
    print(f"Desktop limit compliance: {'OK' if desktop_valid else 'Exceeds limit'}")
    print(f"Mobile limit compliance: {'OK' if mobile_valid else 'Exceeds limit'}")
    
    if potential_issues:
        print("\nPotential compliance issues:")
        for issue in potential_issues:
            print(f"- {issue['description']} (found: '{issue['found']}')")
    
    # Prepare message for compliance review
    message = f"""I need to review content for our Agent Brown Savings customers. Here's the draft:

    "{example_content}"

    Current word count: {word_count} words
    Desktop word limit: {desktop_limit} (Status: {'OK' if desktop_valid else 'Exceeds limit'})
    Mobile word limit: {mobile_limit} (Status: {'OK' if mobile_valid else 'Exceeds limit'})
    {issues_text}
    Please review this for compliance with UK banking regulations and provide feedback."""
    
    print("\n\nSending to compliance reviewer...\n")
    
    # Start the conversation
    user_proxy.initiate_chat(
        compliance_agent,
        message=message
    )

if __name__ == "__main__":
    run_example()
