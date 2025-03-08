# Banking Content Compliance Review System

A multi-agent system for reviewing Agent Brown Savings (ABrown Group) banking content against UK compliance rules.

## Overview

This system uses Autogen to implement a set of AI agents that:

1. Takes a rough outline of content for Agent Brown Savings customers
2. Takes word count requirements for desktop browser and mobile app
3. Reviews the content for UK compliance rules

The system currently includes:
- A Compliance Reviewer agent that checks content against UK banking regulations
- A Content Creator agent that can refine content based on compliance feedback
- Utilities for word count validation and compliance rule checking

## Quick Setup

### For Unix/Linux/Mac:
```bash
./setup.sh
```

### For Windows:
```
setup.bat
```

These scripts will:
1. Create a virtual environment
2. Install dependencies
3. Set up your env.local file with your OpenAI API key
4. Run tests to verify everything is working

## Manual Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create an env.local file with your OpenAI API key:
```bash
cp env.environment env.local
```

5. Edit the env.local file to add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

6. Run the test script to verify your setup:
```bash
python test_setup.py
```

## Usage

### Main Application

Run the main script:
```bash
python main.py
```

The script will:
1. Prompt you to enter your content draft
2. Ask for word count requirements for desktop and mobile
3. Analyze the content for compliance issues
4. Provide a detailed compliance review

### Example Scripts

The repository includes example scripts to demonstrate the system:

- `example.py`: Demonstrates the compliance reviewer with a predefined example
- `workflow_example.py`: Shows a complete workflow with both compliance reviewer and content creator agents

Run them with:
```bash
python example.py
# or
python workflow_example.py
```

## File Structure

```
├── main.py                  # Main orchestration script
├── example.py               # Example script with predefined content
├── workflow_example.py      # Example of complete workflow
├── test_setup.py            # Test script to verify setup
├── setup.sh                 # Setup script for Unix/Linux/Mac
├── setup.bat                # Setup script for Windows
├── env.local                # Environment variables (not in repo)
├── env.environment          # Environment variables template
├── requirements.txt         # Project dependencies
├── agents/                  # Agent implementations
│   ├── compliance_reviewer.py  # Compliance Reviewer agent
│   └── content_creator.py      # Content Creator agent
└── utils/                   # Utility functions
    ├── word_count.py        # Word count validation utilities
    └── compliance_rules.py  # Compliance rule definitions
```

## Configuration

The system uses GPT-4o-mini by default. To use a different model, modify the config_list in main.py:

```python
config_list = [
    {
        "model": "your-preferred-model",
        "api_key": openai_api_key
    }
]
```

## Future Enhancements

Future versions will include additional reviewers such as:
- Legal reviewer
- Customer experience reviewer
- Brand consistency reviewer

## License

[Specify your license here]
