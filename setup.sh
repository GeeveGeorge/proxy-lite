#!/bin/bash

# Install the package in development mode
pip install -e .

# Install Playwright browsers with specific arguments for cloud environment
python -m playwright install --with-deps chromium
python -m playwright install-deps

# Set permissions for Chromium in Streamlit Cloud
mkdir -p $HOME/.cache/ms-playwright
chmod -R 777 $HOME/.cache/ms-playwright

echo "Setup complete!"
