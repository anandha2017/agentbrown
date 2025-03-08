#!/usr/bin/env python3
"""
Banking Content Compliance Review System for Agent Brown Savings (ABrown Group)
This script orchestrates a multi-agent system that reviews content against UK banking compliance rules.
"""

import os
import json
import dotenv
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Import our custom modules
from agents.compliance_reviewer import create_compliance_reviewer_agent, analyze_compliance
from agents.content_creator import create_content_creator_agent, refine_content
from utils.word_count import validate_word_count, get_word_count_status, suggest_content_reduction
from utils.compliance_rules import check_common_issues, get_all_compliance_rules

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

# Create our agents
compliance_agent = create_compliance_reviewer_agent(config_list)
content_creator = create_content_creator_agent(config_list)

# Create a user proxy that can interact with both the human user and the agents
user_proxy = UserProxyAgent(
    name="BankingContentManager",
    human_input_mode="ALWAYS",  # Allow human input for all messages
    code_execution_config={"last_n_messages": 3, "work_dir": ".", "use_docker": False},
    system_message="""You help manage content for Agent Brown Savings banking customers.
    You'll submit content drafts and word count requirements for review and refinement."""
)

def main():
    print("Banking Content Compliance Review System")
    print("----------------------------------------")
    print("This system reviews content for Agent Brown Savings against UK banking compliance rules.")
    print("\nPlease provide the following information:")
    
    # Get content from user
    content = input("\nEnter your content draft:\n")
    
    # Get word count requirements
    try:
        desktop_limit = int(input("\nEnter maximum word count for desktop (or 0 for no limit): "))
        if desktop_limit <= 0:
            desktop_limit = None
    except ValueError:
        desktop_limit = None
    
    try:
        mobile_limit = int(input("\nEnter maximum word count for mobile (or 0 for no limit): "))
        if mobile_limit <= 0:
            mobile_limit = None
    except ValueError:
        mobile_limit = None
    
    # Validate word count
    desktop_valid, mobile_valid, word_count = validate_word_count(content, desktop_limit, mobile_limit)
    
    # Check for common compliance issues
    potential_issues = check_common_issues(content)
    issues_text = ""
    if potential_issues:
        issues_text = "\n\nPotential compliance issues detected:\n"
        for issue in potential_issues:
            issues_text += f"- {issue['description']} (found: '{issue['found']}')\n"
    
    # Prepare message for compliance review
    message = f"""I need to review content for our Agent Brown Savings customers. Here's the draft:

    "{content}"

    Current word count: {word_count} words
    Desktop word limit: {desktop_limit if desktop_limit else 'No limit'} (Status: {'OK' if desktop_valid else 'Exceeds limit'})
    Mobile word limit: {mobile_limit if mobile_limit else 'No limit'} (Status: {'OK' if mobile_valid else 'Exceeds limit'})
    {issues_text}
    Please review this for compliance with UK banking regulations and provide feedback."""
    
    # Start the conversation
    user_proxy.initiate_chat(
        compliance_agent,
        message=message
    )

if __name__ == "__main__":
    main()
