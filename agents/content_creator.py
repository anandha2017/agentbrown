"""
Content Creator Agent for Agent Brown Savings Banking Content Compliance Review System
This module defines the Content Creator agent that creates and refines content based on compliance feedback.
"""

from autogen import AssistantAgent

def create_content_creator_agent(config_list):
    """
    Create and return a Content Creator agent
    
    Args:
        config_list: Configuration for the LLM
        
    Returns:
        AssistantAgent: The Content Creator agent
    """
    return AssistantAgent(
        name="ContentCreator",
        system_message="""You are a skilled content writer for Agent Brown Savings banking.
        Your job is to create and refine content based on compliance feedback.
        You understand UK banking regulations and can adapt content to meet compliance requirements
        while maintaining effective messaging.
        
        When creating or refining content, consider:
        - Word count requirements for desktop and mobile
        - Clear, fair, and not misleading language
        - Appropriate risk warnings
        - Accurate representation of financial products
        - Proper disclosure requirements
        - Compliant with Financial Promotion rules
        
        For financial promotions, ensure you follow these key principles:
        1. Be clear, fair and not misleading
        2. Include appropriate risk warnings
        3. Balance benefits and risks
        4. Avoid absolute or unsubstantiated claims
        5. Include all necessary information for informed decisions
        6. Use plain language and avoid jargon
        
        When word count requirements differ between desktop and mobile:
        - Create a comprehensive version for desktop
        - Create a concise version for mobile that maintains all required compliance elements
        - Ensure both versions convey the same key information and comply with regulations
        
        Provide both desktop and mobile versions when word count requirements differ.""",
        llm_config={"config_list": config_list}
    )

def refine_content(content, compliance_feedback, desktop_limit=None, mobile_limit=None):
    """
    Helper function to refine content based on compliance feedback and word count limits
    
    Args:
        content: Original content
        compliance_feedback: Feedback from compliance review
        desktop_limit: Maximum word count for desktop
        mobile_limit: Maximum word count for mobile
        
    Returns:
        dict: Refined content for desktop and mobile
    """
    # This function would typically be used to process content before sending to the agent
    # In the current implementation, this is handled directly by the agent
    return {
        "original": content,
        "compliance_feedback": compliance_feedback,
        "desktop_limit": desktop_limit,
        "mobile_limit": mobile_limit
    }
