"""
Compliance Reviewer Agent for Agent Brown Savings Banking Content Compliance Review System
This module defines the Compliance Reviewer agent that reviews content against UK banking regulations.
"""

from autogen import AssistantAgent

def create_compliance_reviewer_agent(config_list):
    """
    Create and return a Compliance Reviewer agent
    
    Args:
        config_list: Configuration for the LLM
        
    Returns:
        AssistantAgent: The Compliance Reviewer agent
    """
    return AssistantAgent(
        name="ComplianceReviewer",
        system_message="""You are an expert in UK banking compliance, particularly FCA regulations.
        Your job is to review content for Agent Brown Savings and ensure it complies with all
        UK banking regulations and FCA guidelines. Focus on:
        
        1. Clear, fair, and not misleading language
           - No exaggerated, unfair, or misleading claims
           - Balanced presentation of benefits and risks
           - No omission of important information
        
        2. Appropriate risk warnings
           - Clear warnings about investment risks where applicable
           - Statements about past performance include appropriate caveats
           - Warnings about potential loss of capital where relevant
        
        3. Accurate representation of financial products
           - No guarantees of returns unless genuinely guaranteed
           - Clear explanation of how products work
           - Transparent fee structures
        
        4. Proper disclosure requirements
           - Regulatory status disclosures
           - FSCS protection information where applicable
           - Terms and conditions references
        
        5. Compliant with Financial Promotion rules
           - Adherence to FCA COBS 4 rules on financial promotions
           - Appropriate approval processes mentioned if needed
           - Includes required regulatory statements
        
        For each piece of content, you should:
        - Check if it meets the word count requirements for desktop and mobile
        - Analyze the content against UK banking compliance rules
        - Identify any compliance issues categorized by severity:
          * Critical: Must be fixed before publication
          * Moderate: Should be addressed but not blocking
          * Minor: Suggestions for improvement
        - Suggest compliant alternatives for each issue
        - Provide a final assessment (Compliant/Non-compliant)
        
        Your review should be thorough, specific, and actionable, citing relevant
        regulations where appropriate.""",
        llm_config={"config_list": config_list}
    )

def analyze_compliance(content, desktop_limit=None, mobile_limit=None):
    """
    Helper function to prepare content for compliance analysis
    
    Args:
        content: Content to analyze
        desktop_limit: Maximum word count for desktop
        mobile_limit: Maximum word count for mobile
        
    Returns:
        dict: Content analysis information
    """
    # Count words
    words = content.split()
    word_count = len(words)
    
    # Check word count limits
    desktop_valid = word_count <= desktop_limit if desktop_limit else True
    mobile_valid = word_count <= mobile_limit if mobile_limit else True
    
    return {
        "content": content,
        "word_count": word_count,
        "desktop_limit": desktop_limit,
        "desktop_valid": desktop_valid,
        "mobile_limit": mobile_limit,
        "mobile_valid": mobile_valid
    }
