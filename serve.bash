#!/bin/bash

# serve.bash - Simple script to run the Django webserver
# Run with: . serve.bash
# 
# Starts the Django development server on all interfaces (0.0.0.0) 
# on port 8335 (approximately "BEES")

echo "Starting Django development server on port 8335 (BEES)..."
uv run python manage.py runserver 0.0.0.0:8335