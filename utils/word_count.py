"""
Word Count Utilities for Agent Brown Savings Banking Content Compliance Review System
This module provides utilities for word count validation and processing.
"""

def count_words(text):
    """
    Count the number of words in a text
    
    Args:
        text (str): The text to count words in
        
    Returns:
        int: The number of words in the text
    """
    if not text:
        return 0
    
    # Split by whitespace and count non-empty words
    words = [word for word in text.split() if word.strip()]
    return len(words)

def validate_word_count(content, desktop_limit=None, mobile_limit=None):
    """
    Validate if content meets word count requirements
    
    Args:
        content (str): The content to validate
        desktop_limit (int, optional): Maximum word count for desktop
        mobile_limit (int, optional): Maximum word count for mobile
        
    Returns:
        tuple: (desktop_valid, mobile_valid, word_count)
    """
    word_count = count_words(content)
    
    desktop_valid = word_count <= desktop_limit if desktop_limit else True
    mobile_valid = word_count <= mobile_limit if mobile_limit else True
    
    return (desktop_valid, mobile_valid, word_count)

def get_word_count_status(content, desktop_limit=None, mobile_limit=None):
    """
    Get detailed word count status information
    
    Args:
        content (str): The content to analyze
        desktop_limit (int, optional): Maximum word count for desktop
        mobile_limit (int, optional): Maximum word count for mobile
        
    Returns:
        dict: Word count status information
    """
    desktop_valid, mobile_valid, word_count = validate_word_count(content, desktop_limit, mobile_limit)
    
    return {
        "word_count": word_count,
        "desktop_limit": desktop_limit,
        "desktop_valid": desktop_valid,
        "desktop_status": "OK" if desktop_valid else f"Exceeds limit by {word_count - desktop_limit} words",
        "mobile_limit": mobile_limit,
        "mobile_valid": mobile_valid,
        "mobile_status": "OK" if mobile_valid else f"Exceeds limit by {word_count - mobile_limit} words"
    }

def suggest_content_reduction(content, target_word_count):
    """
    Suggest how to reduce content to meet target word count
    
    Args:
        content (str): The original content
        target_word_count (int): Target word count
        
    Returns:
        dict: Suggestions for content reduction
    """
    current_word_count = count_words(content)
    
    if current_word_count <= target_word_count:
        return {
            "needs_reduction": False,
            "current_word_count": current_word_count,
            "target_word_count": target_word_count,
            "reduction_needed": 0,
            "suggestion": "Content already meets word count requirements."
        }
    
    reduction_needed = current_word_count - target_word_count
    reduction_percentage = (reduction_needed / current_word_count) * 100
    
    suggestion = ""
    if reduction_percentage < 10:
        suggestion = "Minor reduction needed. Consider removing a few adjectives or simplifying sentences."
    elif reduction_percentage < 25:
        suggestion = "Moderate reduction needed. Focus on core message and remove secondary details."
    else:
        suggestion = "Significant reduction needed. Completely rethink the content to focus only on essential information."
    
    return {
        "needs_reduction": True,
        "current_word_count": current_word_count,
        "target_word_count": target_word_count,
        "reduction_needed": reduction_needed,
        "reduction_percentage": reduction_percentage,
        "suggestion": suggestion
    }
