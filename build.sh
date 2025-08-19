#!/bin/bash
set -e  # Exit immediately if any command fails

# Run commands in sequence
echo "Running command 1..."
pip install -r requirements.txt

echo "Running command 2..."
python manage.py collectstatic --noinput

echo "Running command 3..."
python manage.py migrate
