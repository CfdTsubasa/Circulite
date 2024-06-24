#!/bin/bash

# Change to the user's home directory
cd /Users/iijima/

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Change to the Django project directory
cd /Users/iijima/Documents/GitHub/Circulite/

# Run the Django development server
python3 manage.py runserver 8080
