from compliance_system import ComplianceSystem
import pytest

@pytest.fixture
def system():
    return ComplianceSystem()

def test_risk_disclosure_check(system):
    content = "Get guaranteed high returns with our premium savings account!"
    log = system.review_content(content)
    
    assert any(entry['decision'] == "REJECTED" for entry in log), "Should flag absolute guarantees"
    
def test_proper_disclosures(system):
    content = """Kent Reliance Easy Access Saver:
    - FCA regulated
    - FSCS protected up to £85,000
    - 3.5% AER variable rate"""
    
    log = system.review_content(content)
    assert all(entry['decision'] == "APPROVED" for entry in log), "Valid disclosures should pass"

def test_mobile_content_length(system):
    long_content = "Lorem ipsum dolor sit amet " * 100  # 2500+ chars
    log = system.review_content(long_content)
    assert any("CONTENT_LENGTH_WARNING" in entry['message'] for entry in log), "Should flag mobile content length"

def test_error_handling(system):
    invalid_content = 12345  # Non-string input
    with pytest.raises(TypeError):
        system.review_content(invalid_content)
