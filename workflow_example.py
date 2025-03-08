#!/usr/bin/env python3
"""
Workflow Example for the Banking Content Compliance Review System
This script demonstrates a complete workflow using both compliance reviewer and content creator agents.
"""

import os
import json
import dotenv
from autogen import UserProxyAgent, GroupChat, GroupChatManager

# Import our custom modules
from agents.compliance_reviewer import create_compliance_reviewer_agent
from agents.content_creator import create_content_creator_agent
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

def run_workflow_example():
    print("Banking Content Compliance Review System - Workflow Example")
    print("----------------------------------------------------------")
    
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
    
    # Create our agents
    compliance_agent = create_compliance_reviewer_agent(config_list)
    content_creator = create_content_creator_agent(config_list)
    
    # Create a user proxy
    user_proxy = UserProxyAgent(
        name="BankingContentManager",
        human_input_mode="NEVER",  # No human input for this example
        code_execution_config={"last_n_messages": 3, "work_dir": ".", "use_docker": False},
        system_message="""You are managing content for Agent Brown Savings banking customers.
        You'll coordinate between the compliance reviewer and content creator."""
    )
    
    # Set up the group chat
    groupchat = GroupChat(
        agents=[user_proxy, compliance_agent, content_creator],
        messages=[],
        max_round=10
    )
    
    # Create the group chat manager
    manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})
    
    # Validate word count
    desktop_valid, mobile_valid, word_count = validate_word_count(example_content, desktop_limit, mobile_limit)
    
    # Check for common compliance issues
    potential_issues = check_common_issues(example_content)
    issues_text = ""
    if potential_issues:
        issues_text = "\n\nPotential compliance issues detected:\n"
        for issue in potential_issues:
            issues_text += f"- {issue['description']} (found: '{issue['found']}')\n"
    
    # Prepare initial message
    initial_message = f"""We need to review and refine content for Agent Brown Savings customers.

Original Content:
"{example_content}"

Current word count: {word_count} words
Desktop word limit: {desktop_limit} (Status: {'OK' if desktop_valid else 'Exceeds limit'})
Mobile word limit: {mobile_limit} (Status: {'OK' if mobile_valid else 'Exceeds limit'})
{issues_text}

Workflow:
1. ComplianceReviewer: Please review this content for compliance with UK banking regulations
2. ContentCreator: Based on the compliance review, create revised versions for desktop and mobile
3. ComplianceReviewer: Review the revised content
4. Summarize the final compliant versions for desktop and mobile

Let's start with the compliance review.
"""
    
    print("\nStarting the workflow...\n")
    print("-" * 50)
    
    # Start the conversation
    user_proxy.initiate_chat(
        manager,
        message=initial_message
    )

if __name__ == "__main__":
    run_workflow_example()
