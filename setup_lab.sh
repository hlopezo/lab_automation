#!/bin/bash

echo "Initializing Lab Environment..."

# Create virtual environment
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "Virtual environment created."
fi

# Install dependencies
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Initialize project directories
mkdir -p src data data/raw data/prepared data/features models tests .github/workflows

echo "Environment setup complete!"
echo "Run 'source .venv/bin/activate' to start working."
