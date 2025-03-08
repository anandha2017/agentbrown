I want to implement a set of agents that does the following

Context - I work for a UK regulated bank. ABrown Group

Input
1. A rough outline of a piece of content for our customers. Either before or after logging in. For our Agent Brown Savings brand.
2. A rough number of words for desktop browser, and mobile app

Process
3. Act like the worlds best compliance person and review the copy content for UK compliance rules only

I will add additional reviewers in the future. 

Use Python and Autogen. 


Starter Code

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Configure the AI model settings (you'll need your API key configured)
config_list = config_list_from_json("azure_openai_config.json")

# Create a compliance reviewer agent
compliance_agent = AssistantAgent(
    name="ComplianceReviewer",
    system_message="""You are an expert in UK banking compliance, particularly FCA regulations.
    Your job is to review content for Agent Brown Savings and ensure it complies with all
    UK banking regulations and FCA guidelines. Focus on:
    1. Clear, fair, and not misleading language
    2. Appropriate risk warnings
    3. Accurate representation of financial products
    4. Proper disclosure requirements
    5. Compliant with Financial Promotion rules
    Explain any compliance issues you find and suggest compliant alternatives.""",
    llm_config={"config_list": config_list}
)

# Create a user proxy that can interact with both the human user and the compliance agent
user_proxy = UserProxyAgent(
    name="BankingContentCreator",
    human_input_mode="ALWAYS",  # Allow human input for all messages
    code_execution_config={"last_n_messages": 3, "work_dir": "content"},
    system_message="""You help create content for Agent Brown Savings banking customers.
    You'll submit content drafts for compliance review."""
)

# Start the conversation
user_proxy.initiate_chat(
    compliance_agent,
    message="""I need to create content for our savings account page. Here's my draft:

    "Grow your money faster with our Premium Saver account. With market-leading rates and 
    instant access to your funds, there's no better place for your savings. Open an account 
    today with just £100 and watch your money grow!"

    Please review this for compliance with UK banking regulations."""
)