#!/bin/bash

# For development use (simple logging, etc):
# python3 -m pip install -r requirements.txt
# python3 app.py

# For production use: 
gunicorn app -w 1 --log-file -