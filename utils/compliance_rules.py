"""
Compliance Rules Utilities for Agent Brown Savings Banking Content Compliance Review System
This module provides utilities and definitions related to UK banking compliance rules.
"""

# FCA Financial Promotion Rules (COBS 4)
FCA_FINANCIAL_PROMOTION_RULES = {
    "clear_fair_not_misleading": {
        "description": "Financial promotions must be clear, fair and not misleading",
        "details": [
            "Information must be accurate and presented in a way that is not deceptive",
            "Benefits and risks must be presented in a balanced way",
            "Important information must not be hidden or diminished",
            "Avoid using absolute terms like 'best', 'highest', 'guaranteed' unless demonstrably true"
        ],
        "regulation": "FCA COBS 4.2.1R"
    },
    "risk_warnings": {
        "description": "Appropriate risk warnings must be included",
        "details": [
            "Past performance disclaimers where relevant",
            "Capital at risk warnings where appropriate",
            "Warnings about potential loss of investment",
            "Risk warnings must be prominent and not hidden"
        ],
        "regulation": "FCA COBS 4.2.4G"
    },
    "product_information": {
        "description": "Products must be accurately represented",
        "details": [
            "Clear explanation of how products work",
            "Transparent fee structures",
            "No guarantees of returns unless genuinely guaranteed",
            "Clear explanation of terms and conditions"
        ],
        "regulation": "FCA COBS 4.5.2R"
    },
    "disclosure_requirements": {
        "description": "Required disclosures must be included",
        "details": [
            "Regulatory status disclosures",
            "FSCS protection information where applicable",
            "Terms and conditions references",
            "Information about complaints procedures"
        ],
        "regulation": "FCA COBS 4.5.7R"
    }
}

# Common compliance issues and suggested fixes
COMMON_COMPLIANCE_ISSUES = {
    "absolute_claims": {
        "description": "Using absolute or unsubstantiated claims",
        "examples": ["best rates", "highest returns", "guaranteed growth", "no better place"],
        "fixes": [
            "Add qualifying language (e.g., 'one of the best', 'competitive rates')",
            "Provide evidence for claims (e.g., 'award-winning service since 2020')",
            "Remove absolute claims entirely"
        ]
    },
    "missing_risk_warnings": {
        "description": "Missing appropriate risk warnings",
        "examples": ["Invest now", "Watch your money grow", "Start earning today"],
        "fixes": [
            "Add appropriate risk warnings",
            "Include capital at risk statements",
            "Add past performance disclaimers"
        ]
    },
    "unbalanced_presentation": {
        "description": "Unbalanced presentation of benefits and risks",
        "examples": ["Only mentioning benefits without risks", "Emphasizing returns without mentioning potential losses"],
        "fixes": [
            "Balance benefits with appropriate risk information",
            "Give equal prominence to risks and benefits",
            "Ensure risks are not hidden or diminished"
        ]
    },
    "misleading_rates": {
        "description": "Misleading presentation of rates or returns",
        "examples": ["Headline rates that are not available to all", "Promotional rates without mentioning time limitations"],
        "fixes": [
            "Clearly state conditions for rates",
            "Include time limitations for promotional rates",
            "Explain eligibility criteria"
        ]
    },
    "missing_disclosures": {
        "description": "Missing required disclosures",
        "examples": ["No regulatory status", "No FSCS information", "No terms and conditions reference"],
        "fixes": [
            "Add regulatory status disclosure",
            "Include FSCS protection information where applicable",
            "Add terms and conditions reference"
        ]
    }
}

def check_common_issues(content):
    """
    Check content for common compliance issues
    
    Args:
        content (str): The content to check
        
    Returns:
        list: List of potential compliance issues found
    """
    content_lower = content.lower()
    issues = []
    
    for issue_key, issue_data in COMMON_COMPLIANCE_ISSUES.items():
        for example in issue_data["examples"]:
            if example.lower() in content_lower:
                issues.append({
                    "type": issue_key,
                    "description": issue_data["description"],
                    "found": example,
                    "fixes": issue_data["fixes"]
                })
                break
    
    return issues

def get_compliance_rule_details(rule_key):
    """
    Get details for a specific compliance rule
    
    Args:
        rule_key (str): The key for the compliance rule
        
    Returns:
        dict: Details of the compliance rule
    """
    return FCA_FINANCIAL_PROMOTION_RULES.get(rule_key, {})

def get_all_compliance_rules():
    """
    Get all compliance rules
    
    Returns:
        dict: All compliance rules
    """
    return FCA_FINANCIAL_PROMOTION_RULES
