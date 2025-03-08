#!/usr/bin/env python3
"""
Test Setup Script for Banking Content Compliance Review System
This script tests the basic setup and components of the system.
"""

import os
import sys
import json
import dotenv

def test_environment():
    """Test environment variables and dependencies"""
    print("Testing environment setup...")
    
    # Check Python version
    python_version = sys.version.split()[0]
    print(f"Python version: {python_version}")
    
    # Check if dotenv is working
    try:
        dotenv.load_dotenv('env.local')
        print("✓ dotenv loaded successfully")
    except Exception as e:
        print(f"✗ Error loading dotenv: {e}")
        return False
    
    # Check OpenAI API key
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        print("✗ OPENAI_API_KEY not found in environment variables")
        return False
    elif openai_api_key == "your_openai_api_key_here":
        print("✗ OPENAI_API_KEY has not been set in env.local")
        return False
    else:
        print("✓ OPENAI_API_KEY found")
    
    return True

def test_imports():
    """Test importing required modules"""
    print("\nTesting imports...")
    
    try:
        import autogen
        print(f"✓ autogen imported successfully (version: {autogen.__version__})")
    except ImportError:
        print("✗ Failed to import autogen. Please install it with: pip install pyautogen")
        return False
    
    try:
        from agents.compliance_reviewer import create_compliance_reviewer_agent
        print("✓ compliance_reviewer module imported successfully")
    except ImportError:
        print("✗ Failed to import compliance_reviewer module")
        return False
    
    try:
        from agents.content_creator import create_content_creator_agent
        print("✓ content_creator module imported successfully")
    except ImportError:
        print("✗ Failed to import content_creator module")
        return False
    
    try:
        from utils.word_count import validate_word_count
        print("✓ word_count module imported successfully")
    except ImportError:
        print("✗ Failed to import word_count module")
        return False
    
    try:
        from utils.compliance_rules import check_common_issues
        print("✓ compliance_rules module imported successfully")
    except ImportError:
        print("✗ Failed to import compliance_rules module")
        return False
    
    return True

def test_word_count():
    """Test word count functionality"""
    print("\nTesting word count functionality...")
    
    from utils.word_count import validate_word_count
    
    test_content = "This is a test sentence with exactly ten words."
    desktop_limit = 15
    mobile_limit = 5
    
    desktop_valid, mobile_valid, word_count = validate_word_count(test_content, desktop_limit, mobile_limit)
    
    if word_count == 10:
        print(f"✓ Word count correct: {word_count}")
    else:
        print(f"✗ Word count incorrect: got {word_count}, expected 10")
        return False
    
    if desktop_valid:
        print(f"✓ Desktop validation correct (under limit of {desktop_limit})")
    else:
        print(f"✗ Desktop validation incorrect")
        return False
    
    if not mobile_valid:
        print(f"✓ Mobile validation correct (over limit of {mobile_limit})")
    else:
        print(f"✗ Mobile validation incorrect")
        return False
    
    return True

def test_compliance_rules():
    """Test compliance rules functionality"""
    print("\nTesting compliance rules functionality...")
    
    from utils.compliance_rules import check_common_issues
    
    test_content = "Our account offers the best rates and guaranteed returns."
    
    issues = check_common_issues(test_content)
    
    if issues and len(issues) >= 1:
        print(f"✓ Compliance issues detected correctly: {len(issues)} issues found")
        for issue in issues:
            print(f"  - {issue['type']}: {issue['found']}")
    else:
        print("✗ Failed to detect compliance issues")
        return False
    
    return True

def run_tests():
    """Run all tests"""
    print("Banking Content Compliance Review System - Setup Test")
    print("---------------------------------------------------")
    
    tests = [
        ("Environment", test_environment),
        ("Imports", test_imports),
        ("Word Count", test_word_count),
        ("Compliance Rules", test_compliance_rules)
    ]
    
    results = []
    
    for name, test_func in tests:
        print(f"\n=== Testing {name} ===")
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"✗ Test failed with error: {e}")
            results.append((name, False))
    
    # Print summary
    print("\n=== Test Summary ===")
    all_passed = True
    for name, result in results:
        status = "PASSED" if result else "FAILED"
        if not result:
            all_passed = False
        print(f"{name}: {status}")
    
    if all_passed:
        print("\n✓ All tests passed! Your system is set up correctly.")
    else:
        print("\n✗ Some tests failed. Please fix the issues before running the system.")

if __name__ == "__main__":
    run_tests()
