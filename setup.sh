#!/bin/bash
# Setup script for Banking Content Compliance Review System

echo "Banking Content Compliance Review System - Setup"
echo "-----------------------------------------------"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Create virtual environment
echo -e "\nCreating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment. Please install venv and try again."
    exit 1
fi

# Activate virtual environment
echo -e "\nActivating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

# Install dependencies
echo -e "\nInstalling dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies."
    exit 1
fi

# Set up env.local file if it doesn't exist
if [ ! -f env.local ]; then
    echo -e "\nSetting up env.local file..."
    cp env.environment env.local
    
    # Prompt for OpenAI API key
    echo -e "\nPlease enter your OpenAI API key:"
    read api_key
    
    # Replace placeholder with actual API key
    if [ -n "$api_key" ]; then
        sed -i.bak "s/your_openai_api_key_here/$api_key/g" env.local
        rm env.local.bak
        echo "API key added to env.local"
    else
        echo "No API key provided. You'll need to edit env.local manually."
    fi
else
    echo -e "\nenv.local file already exists. Skipping setup."
fi

# Run test setup
echo -e "\nRunning setup tests..."
python test_setup.py

echo -e "\nSetup complete!"
echo "To run the system, activate the virtual environment and run main.py:"
echo "source venv/bin/activate"
echo "python main.py"

# Deactivate virtual environment
deactivate
