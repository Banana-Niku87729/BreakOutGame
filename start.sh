#!/bin/bash
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "Running blockout.py..."
python3 blockout.py
echo "blockout.py has finished running."
