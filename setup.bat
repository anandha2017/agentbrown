@echo off
:: Setup script for Banking Content Compliance Review System (Windows)

echo Banking Content Compliance Review System - Setup
echo -----------------------------------------------

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python and try again.
    exit /b 1
)

:: Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Failed to create virtual environment. Please install venv and try again.
    exit /b 1
)

:: Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

:: Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    exit /b 1
)

:: Set up env.local file if it doesn't exist
if not exist env.local (
    echo.
    echo Setting up env.local file...
    copy env.environment env.local

    :: Prompt for OpenAI API key
    echo.
    echo Please enter your OpenAI API key:
    set /p api_key=

    :: Replace placeholder with actual API key
    if defined api_key (
        powershell -Command "(Get-Content env.local) -replace 'your_openai_api_key_here', '%api_key%' | Set-Content env.local"
        echo API key added to env.local
    ) else (
        echo No API key provided. You'll need to edit env.local manually.
    )
) else (
    echo.
    echo env.local file already exists. Skipping setup.
)

:: Run test setup
echo.
echo Running setup tests...
python test_setup.py

echo.
echo Setup complete!
echo To run the system, activate the virtual environment and run main.py:
echo venv\Scripts\activate
echo python main.py

:: Deactivate virtual environment
deactivate

pause
