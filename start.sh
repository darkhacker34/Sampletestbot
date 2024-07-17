#!/bin/bash

# Create downloads directory if it doesn't exist
mkdir -p downloads

# Install required Python packages
pip install pyrogram moviepy

# Run the Python bot
python bot.py
